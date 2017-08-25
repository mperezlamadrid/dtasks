$(document).ready( function() { 
    $('.task-checkbox input[type="checkbox"]').change(function() {
        id = $(this).attr('id').split('-')[1]
        $("#task-done-form-"+id).submit()
    });

    $('.delete-task-button').click(function() {
        var check = confirm("Are you sure?");

        if (check == true) {
            id = $(this).data('pk')
            $("#delete-task-form-"+id).submit()
        }else {
            return false;
        }
    });
});