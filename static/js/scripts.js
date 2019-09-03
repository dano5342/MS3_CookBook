var isOnRecipe = document.getElementsByClassName(".ingredients");
var methodOnRecipe = document.getElementsByClassName(".methods");


if (isOnRecipe.length > 0) {

}
else {
    let ingredientCounter = $(".ingredients").length

    /* Add new ingredient line */
    $(".i-add").click(function() {
        /* append form, insert before add/remove btns and clear existing values */
        $(".ingredients:last").append("<input type='text' name='ingredients' class='ingredients' placeholder='One ingredient per box!'/>")
            .insertBefore(".i-add")
            .find("input[type='text']").val("");
        ingredientCounter += 1;
    });
    /* Remove last ingredients line */
    $(".i-remove").click(function() {
        if (ingredientCounter > 1) {
            $(".ingredients:last").remove();
            ingredientCounter -= 1;
        }
    });
}

if (methodOnRecipe.length > 0) {

}
else {
    let methodCount = $(".methods").length

    /* Add new line */
    $(".m-add").click(function() {
        /* append form, insert before add/remove btns and clear existing values */
        $(".methods:last").append("<input type='text' name='methods' class='methods' required placeholder='Boil water and drop in spaghetti, add balsamic vinegar to bring out a nice tangy flavour...'/>")
            .insertBefore(".m-add")
            .find("input[type='text']").val("");
        methodCount += 1;
    });

    /* Remove last line */
    $(".m-remove").click(function() {
        if (methodCount > 1) {
            $(".methods:last").remove();
            methodCount -= 1;
        }
    });
}
