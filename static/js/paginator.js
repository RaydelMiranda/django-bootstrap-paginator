function Pagination(counter) {

    this.counter = counter;
    this.activeted = 0;

    $("#objects-list>li").hide();
    $("#objects-list>li").slice(0, counter).fadeIn("slow");

    $(".paginator-number").first().addClass("active");
}

Pagination.prototype.paginate = function(init, end){

    $(".paginator-number").removeClass("active");
    $(".paginator-number").slice(init / this.counter, init / this.counter + 1).addClass("active");


    $("#objects-list>li").hide();
    $("#objects-list>li").slice(init, end).fadeIn("slow");

    this.activeted = init / this.counter;

}

Pagination.prototype.next = function(){

    console.log($(".paginator-number").last());
    var elements = $(".paginator-number").slice(++this.activeted, this.activeted);
    console.log(elements.slice(0, 0));
    if (this.activeted >  $(".paginator-number").index($(".paginator-number").last()))
    {
        --this.activeted;
        return;
    }

    $(".paginator-number").removeClass("active");
    elements.addClass("active");
    this.paginate(this.counter * this.activeted, this.counter * this.activeted + this.counter);

}

Pagination.prototype.prev = function(){

    var elements = $(".paginator-number").slice(--this.activeted, this.activeted);
    if (this.activeted <  $(".paginator-number").index($(".paginator-number").first()))
    {
        ++this.activeted;
        return;
    }

    $(".paginator-number").removeClass("active");
    elements.addClass("active");
    this.paginate(this.counter * this.activeted, this.counter * this.activeted + this.counter);
}
