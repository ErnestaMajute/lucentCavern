$(document).ready(function () {
 // # Function from BoutiqueAdo mini project
    $('#sort-selector').change(function () {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if (selectedVal != "reset") {
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    });

    // Disable +/- buttons outside 1-20 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 19;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    };

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for (var i = 0; i < allQtyInputs.length; i++) {
        var itemId = $(allQtyInputs[i]).data('item_id');
        handleEnableDisable(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function () {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function (e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Update quantity on click
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });
});