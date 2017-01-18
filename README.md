# A Bootstrap/Jquery paginator.

Django built in paginator require to make a new request to the server
each time we browse pages.On the other hand, create a paginator using 
JS is a tedious task, that can be very repetitive.

Whit this application the author intends to simplify the effort needed for
create a good looking and easy to use paginator.


## Usage.

Just add paginator to your installed apps.

```python
INSTALLED_APPS = [
    ... 
    'pagintor',
    ...
]
```


The syntax of the tag is as follow:

```twig
{% load paginator %}
{% paginate <sequence> <objects per page>  <L|T> %}
    # Here you can write the code for render a single item.
    # Each item is accessible in this context through the variable
    # paginator_item. 
{% endpaginate%}
```

**sequence:** A sequence of objects to paginate.
**objects per page:** How many objects will be shown per page.
**L|T:** Show objects in **L**inear or **T**abular format.

Example:
----------------

```twig
{% paginate people 10 T%}
    <div>
        Name: {{ paginator_imte.name }} <br/>
        Age: {{ paginator_imte.age }}
    </div>
{% end paginate%}
```