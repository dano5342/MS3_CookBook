let ingCount = $(".ingredients").length;

/* Add new line */
$(".i-add").click(function() {
    /* Clone line, insert before add/remove btns and clear existing values */
    $(".ingredient:first").clone()
        .insertAfter(".ingredient")
        .find("input[type='text']").val("");
    /* Ensures original line is never removed */
    ingCount += 1;
});


/* Remove last line */
$(".i-remove").click(function() {
    /* Ensure that the first line can't be removed */
    if (ingCount > 1) {
        $(".ingredients:last").remove();
        ingCount -= 1;
    }
});
