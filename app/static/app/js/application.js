$(document).ready( function() {
    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.task-checkbox input[type="checkbox"]').change(function() {
        id = $(this).attr('id').split('-')[1]

        $.ajax({
            url: "/task_done/"+id+"/",
            type: "PUT"
        }).done(function(data) {
            $(".title-task-item.task-"+data['todo_id']).removeClass('check')
            $(".title-task-item.task-"+data['todo_id']).removeClass('uncheck')

            if(data['updated']){
                $(".title-task-item.task-"+data['todo_id']).addClass('check')
            }else{
                $(".title-task-item.task-"+data['todo_id']).addClass('uncheck')
            }
        }).fail(function(data){
            $("#todo-"+id).prop('checked', true);
            $('#error-modal').modal('show');
        });
    });

    $('.delete-task-button').click(function() {
        var check = confirm("Are you sure?");
        task_box = $(this).closest('.title-task-item').parent();     
        if (check == true) {
            id = $(this).data('pk')

            $.ajax({
                url: "/delete_task/"+id,
                type: "DELETE"
            }).done(function(data) {
                task_box.remove()
            });
        }else {
            return false;
        }
    });

    $('.delete-list-button').click(function(e) {
        e.preventDefault();

        var check = confirm("Are you sure?");
        list_box = $(this).closest('.delete-list').parent();     
        if (check == true) {
            id = $(this).data('pk')

            $.ajax({
                url: "/delete_list/"+id,
                type: "DELETE"
            }).done(function(data) {
                list_box.remove();
            });
        }else {
            return false;
        }
    });
});