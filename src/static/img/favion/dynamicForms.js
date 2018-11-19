// javascript
// Resources used in this example:
// http://net.tutsplus.com/tutorials/javascript-ajax/submit-a-form-without-page-refresh-using-jquery/



// I put this on the template page so it can be manipulated with context. I wouldn't suggest doing that

 function getCookie(name) {
// get the csrf token

    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
            $(":input").change(function() {
                // validate and process form

                var title = $("input#id_title").val();
                if (title == "") {
                    $("#div_id_title").addClass('error');
                    $("input#id_title").after('<span class="help-inline">Title required</span>');
                    $("input#id_title").focus();
                    return false;
                } else {
                    $('.help-inline').remove();
                    $("#div_id_title").removeClass('error');
                }

                var description = $("textarea#id_description").val();
                if (description == "") {
                    $("div_id_description").addClass('error');
                    $("textarea#id_description").after('<span class="help-inline">Required</span>');
                    $("textarea#id_description").focus();
                    	return false;
            }  else {
                $('.help-inline').remove();
                    $("div_id_description").removeClass('error');
            }

                var dataString =
                        'title='+ title
                                + '&description=' + description
                                + '&csrfmiddlewaretoken=' + getCookie('csrftoken');
                
                $.ajax({
                    // django mixin
                    type: "POST",
                    url: "{% url 'task-update' task.id %}",
                    data: dataString,
                    success: function() {
                        $('#message).html("<ul id=\'message\'></ul>")
                                .hide()
                                .fadeIn(1500);
                        $.getJSON("{% url 'task-ajax-detail' task.id %}",function(result){
                            $.each(result, function(i, field){
                                $("#result").append("<li>" + i + " : " + field + "</li>");
                            });
                        });
                    }
                });
                return false;
            });
        });
        runOnLoad(function(){
            $("input#id_title").select().focus();
        });
