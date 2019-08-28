let ingCount = $(".ingredients").length;

/* Add new ingredient line */
$(".i-add").click(function() {
    /* Clone line, insert before add/remove btns and clear existing values */
    $(".ingredients:first").append("<form class='ingredients'> <input type='text' name='ingredients' /> </form>")
        .insertBefore(".i-add")
        .find("input[type='text']").val("");
    /* Ensures original line is never removed */
    ingCount += 1;
});
/* Remove last ingredients line */
$(".i-remove").click(function() {
    /* Ensure that the first line can't be removed */
    if (ingCount > 1) {
        $(".ingredients:last").remove();
        ingCount -= 1;
    }
});


let methodCount = $(".method").length;

/* Add new line */
$(".m-add").click(function() {
    /* Clone line, insert before add/remove btns and clear existing values */
    $(".method:first").append("<form class='method'> <input type='text' name='method' /> </form>")
        .insertBefore(".m-add")
        .find("input[type='text']").val("");
    /* Ensures original line is never removed */
    methodCount += 1;
});

/* Remove last line */
$(".remove-instruction").click(function() {
    /* Ensure that the first line can't be removed */
    if (methodCount > 1) {
        $(".method:last").remove();
        methodCount -= 1;
    }
});
