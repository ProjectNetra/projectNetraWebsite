$(document).ready(function () {
    const fadeInOut = (element, callback, callback2 = null) => {
        element.fadeOut(function () {
            callback();
            element.fadeIn(callback2);
        })
    }
    $(".expand-project").click(function (e) {
        e.preventDefault();
        const $this = $(this);
        const divToCollapse = $(`#${$this.attr("coll")}`);
        const divToExpand = $(`#${$this.attr("exp")}`);
        const project = $(`#${$this.attr("project")}`);
        divToCollapse.css('overflow-y', 'hidden');
        const a = divToCollapse.find('.home-content .home-desc')
        a.addClass('right');
        divToCollapse.velocity({
            opacity: '0%',
        }, {
            duration: 500,
        }).then(() => {
            divToCollapse.addClass("hidden");
            divToExpand.removeClass("hidden");
            divToExpand.velocity({
                opacity: '100%'
            })
        }).then(() => {
            a.removeClass('right');
        });

    })
    $(".collapse-project").click(function (e) {
        e.preventDefault();
        const $this = $(this);
        const divToCollapse = $(`#${$this.attr("coll")}`);
        const divToExpand = $(`#${$this.attr("exp")}`);
        const project = $(`#${$this.attr("project")}`);
        const b = divToExpand.find('.desc1');
        b.addClass('left');
        divToExpand.velocity({
            opacity: '0%',
        }, {
            duration: 500,
        }).then(() => {
            divToExpand.addClass("hidden");
            divToCollapse.removeClass("hidden");
            divToCollapse.velocity({
                opacity: '100%'
            })
        }).then(() => {
            b.removeClass('left');
        });
    })
    $(".carousel-button").each(function () {
        const $this = $(this);
        const divToCollapse = $(`#${$this.attr("coll")}`);
        const divToExpand = $(`#${$this.attr("exp")}`);
        const project = $(`#${$this.attr("project")}`);
        let currBgImage = project.find(`.meta.hidden carousel imgUrl`).first();
        const BgUrl = (imageUrl) => imageUrl.text();
        divToExpand.children('picture').css('background-image', `url(${BgUrl(currBgImage)})`);

        $this.children('.carousel-next').click(function () {
            currBgImage = currBgImage.next().length ? currBgImage.next() : currBgImage;
            console.log(currBgImage, BgUrl(currBgImage));
            divToExpand.children('.picture').css('background-image', `url(${BgUrl(currBgImage)})`);
        });
        $this.children('.carousel-previous').click(function () {
            currBgImage = currBgImage.prev().length ? currBgImage.prev() : currBgImage;
            console.log(currBgImage, BgUrl(currBgImage));
            divToExpand.children('.picture').css('background-image', `url(${BgUrl(currBgImage)})`);
        });
    })
})
