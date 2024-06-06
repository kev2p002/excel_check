.strikeout {
    text-decoration: line-through;
}

.rationale-input {
    text-decoration: none;
}$(document).on('change', '.interaction-dropdown', function() {
    var row = $(this).closest('tr');
    var interactionValue = $(this).val();
    
    if (interactionValue === 'No Interaction') {
        row.find('td').each(function(index) {
            if (index !== 3) { // Avoid applying strikeout to the Rationale column
                $(this).addClass('strikeout');
            }
        });
    } else {
        row.find('td').removeClass('strikeout');
    }
});
