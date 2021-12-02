$(document).ready(function () {

    $("form.ajax").on("submit",function(event){
        event.preventDefault();
        var $this = $(this);

        var url = $this.attr("action")
        var method = $this.attr("method")

        jQuery.ajax({
            type:method,
            url:url,
            dataType:"json",
            data:new FormData(this),
            processData : false,
            contentType : false,
            cache : false,

            success:function(data){

                var title = data["title"]
                var text = data["message"]
                var status = data["status"]

                Swal.fire({
                    icon: status,
                    title: title,
                    text : text
                  })
                  
                if (status == "success"){
                    $this.trigger("reset");
                }
            },
            error : function(data){

            }
        })
    });


    // $( "a.category" ).click(function(event) {
    //     event.preventDefault();

    //     var category = $this.attr("category")

    //     $.ajax({
    //         url: "{% url 'web:index' %}?category={{category.name}}",
    //         method: 'GET',
    //         data : {
    //             projects = projects.filter(category__name=category_name)
    //         },
    //         success: function(data){
    //             console.log(data)
    //         },
    //         error: function(xhr, errmsg, err){
    //             console.log("error")
    //             console.log(error_data)
    //         }
    //    });
    // });
});