$(document).on("submit","form.ajax", function(e) {
    e.preventDefault();
    var $this = $(this);

    var url = $this.attr("action");
    var method = $this.attr("method");

    jQuery.ajax({
        type: method,
        url:url,
        datatype:"json",
        data: new FormData(this),
        processData:false,
        contentType: false,
        cache: false,
        success:function(data) {
            let datas = JSON.parse(data)  
            console.log(data);

            // var title = datas["title"];
            // var message = datas["message"];
            // var status = datas["status"];

            var title =datas.title;
            var message =datas.message;
            var status =datas.status;

            Swal.fire({
                icon: status,
                title: title,
                text: message,
              })

              if(status=="success"){
                $this.trigger("reset");
              }
        },
        error: function(error) {
            console.log("errorr");
        },
    });
}) ;










