from django import template
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


class PaginationNode(template.Node):

    def __init__(self, sequence, page_count, mode, nodelist):
        self.nodelist = nodelist
        self.sequence = template.Variable(sequence)
        self.page_count = page_count
        self.mode = mode.upper()

        self.modes = {
            'T': "paginator/paginator-tabular.html",
            'L': "paginator/paginator.html",
        }

    def __iter__(self):
        for node in self.nodelist:
            yield node

    def render(self, context):

        with context.push():

            try:
                values = self.sequence.resolve(context)
            except template.VariableDoesNotExist:
                values = []
            if values is None:
                values = []
            if not hasattr(values, '__len__'):
                values = list(values)
            len_values = len(values)
            if len_values < 1:
                return []   # TODO: Make node for empty.

            nodelist = []
            rendered_items = []

            default_item_template = context.template.engine.get_template("paginator/default_item_layout.html")
            render_default = False
            for i, item in enumerate(values):
                context['paginator_item'] = item

                for node in self.nodelist:
                    nodelist.append(node.render_annotated(context))

                rendered_nodes = mark_safe(''.join(force_text(n.render(context)) for n in self.nodelist))
                if all([c.isspace() for c in rendered_nodes]):
                    rendered_items.append(default_item_template.render(context))
                else:
                    rendered_items.append(mark_safe(rendered_nodes))

        context['rendered_items'] = rendered_items
        context['page_count'] = self.page_count
        context['page_ranges'] = range(0, len_values, int(self.page_count))
        t = context.template.engine.get_template(self.modes[self.mode])
        return t.render(context)


def do_pagination(parser, token):

    try:
        tag_name, sequence, page_count, mode = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires exactly one argument" % token.contents_split()[0]
        )

    nodelist = parser.parse(('endpaginate',))
    parser.delete_first_token()

    return PaginationNode(sequence, page_count, mode, nodelist=nodelist)


register.tag('paginate', do_pagination)
