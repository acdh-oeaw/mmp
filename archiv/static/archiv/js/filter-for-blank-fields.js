$(function()
{
    var form = $( 'form' )[0];
    $( form ).submit(function() 
    { 
        $('input, select').each(function()
        {
            if ($(this).val().length === 0) 
            {
                $(this).prop('disabled', true);
                $(this).next().prop('disabled', true);
            }
        });
    });
});