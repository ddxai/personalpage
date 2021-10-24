$(document).ready(function() {
    $('img.size-category').click(function() {
        let active_item=document.getElementsByClassName('active carousel-item')[0]
        if (active_item != undefined) { active_item.classList.remove('active') }
        let img_id=$(this).attr('id').slice(-1)
        let carousel_id='carousel-item-' + img_id
        document.getElementById(carousel_id).classList.add('active')
        $('#myModal').modal('show');
    })
});
