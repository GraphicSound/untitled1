/**
 * Created by yu on 12/11/14.
 */

// my.js

$(function() {
    // 所有页面都会共享执行的代码段
});

function background_page_ready() {

}

function stage_page_ready() {
    // 拉取用户作品信息
    get_info();
    get_showcase();
    get_note();
}

function index_page_ready() {
    // 拉取最新职位和笔记
    link_template = $(".latest-job").find("a").clone();
    get_latest_job(link_template);
    get_latest_note(link_template);
}

function get_latest_job(link_template) {
    latest_job = $(".latest-job");
    latest_job.empty();

    console.log(link_template);
    $.ajax({
        url: "/app1/api_latest_job", success: function (res) {
            console.log(res);
            data = JSON.parse(res);
            $.each(data, function(index, item) {
                link_copy = link_template.clone();
                link_copy.attr("href", "/app1/job?id=" + item["id"]);
                link_copy.find("img").attr("src", item["avatar_link"]);
                link_copy.find(".realname").text(item["realname"]);
                link_copy.find(".info").text(item["company_name"]);
                link_copy.find(".title").text(item["title"]);
                link_copy.find(".introduction").text(item["introduction"]);
                latest_job.prepend(link_copy);
            });
        }
    });
}

function get_latest_note(link_template) {
    latest_note = $(".latest-note");

    console.log(link_template);
    $.ajax({
        url: "/app1/api_latest_note", success: function (res) {
            console.log(res);
            data = JSON.parse(res);
            $.each(data, function (index, item) {
                link_copy = link_template.clone();
                link_copy.attr("href", "/app1/stage?user_id=" + item["user_id"]);
                link_copy.find("img").attr("src", item["avatar_link"]);
                link_copy.find(".realname").text(item["realname"]);
                link_copy.find(".info").text(item["add_time"]);
                link_copy.find(".title").text(item["title"]);
                link_copy.find(".introduction").text(item["content"]);
                latest_note.prepend(link_copy);
            });
        }
    });
}

function get_info() {
    $.ajax({
        url: "/app1/api_info", data:{"user_id": $(".user-id").text()}, success: function (res) {
            console.log(res);
            data = JSON.parse(res);
            $.each(data, function (index, item) {
                $(".bg-image").css({
                    "background-image": "url('" + item["background_image_link"] + "')"
                });
                $(".self-realname").text(item["realname"] + "，");
                $(".self-introduction").text(item["introduction"]);
                $(".self-field").text(item["field_description"]);
                $(".self-speciality").text(item["speciality_description"]);
            });
        }
    });
}

function get_showcase() {
    timeline = $(".timeline.animated");
    row_text = $(".row-text").clone();
    row_image = $(".row-image").clone();
    row_video = $(".row-video").clone();
    timeline.empty();

    console.log();
    $.ajax({
        url: "/app1/api_showcase", data:{"user_id": $(".user-id").text()}, success: function (res) {
            console.log(res);
            data = JSON.parse(res);
            $.each(data, function(index, item) {
                link_copy = row_text.clone();
                if(item["link"]) {
                    link_copy = row_image.clone();
                    link_copy.find("img").attr("src", item["link"]);

                }
                link_copy.find(".timeline-time").text(item["finish_time"]);
                link_copy.find(".row-title").text(item["title"]);
                link_copy.find(".row-content").text(item["content"]);
                timeline.prepend(link_copy);
            });

            // 生成时间线
            var timelineAnimate;
            timelineAnimate = function(elem) {
              return $(".timeline.animated .timeline-row").each(function(i) {
                var bottom_of_object, bottom_of_window;
                bottom_of_object = $(this).position().top + $(this).outerHeight();
                bottom_of_window = $(window).scrollTop() + $(window).height();
                if (1 || bottom_of_window > bottom_of_object) {
                  return $(this).addClass("active");
                }
              });
            };
            timelineAnimate();
            return $(window).scroll(function() {
              return timelineAnimate();
            });
        }
    });
}

function get_note() {
    blog = $(".blog-card");
    card = $(".card").clone();
    blog.empty();

    console.log();
    $.ajax({
        url: "/app1/api_note", data:{"user_id": $(".user-id").text()}, success: function (res) {
            console.log(res);
            data = JSON.parse(res);
            $.each(data, function(index, item) {
                link_copy = card.clone();
                if(item["link"]) {
                    link_copy.find(".card-img").attr("src", item["link"]);
                } else {
                    link_copy.find(".card-img").addClass("hidden");
                    link_copy.find("br").addClass("hidden");
                }
                link_copy.find(".panel-heading").text(item["title"]);
                link_copy.find(".card-add-time").text(item["add_time"]);
                link_copy.find(".panel-content").text(item["content"]);
                blog.prepend(link_copy);
            });
        }
    });
}

/* --- EASY FADER --- */

/*
* EASYFADER - An Ultralight Fading Slideshow For Responsive Layouts
* Version: 1.3
* License: Creative Commons Attribution 3.0 Unported - CC BY 3.0
* http://creativecommons.org/licenses/by/3.0/
* This software may be used freely on commercial and non-commercial projects with attribution to the author/copyright holder.
* Author: Patrick Kunka
* Copyright 2013 Patrick Kunka, All Rights Reserved
*/

(function(a) {
    function h(b) {
        for (var a = ["Webkit", "Moz", "O", "ms"], c = 0; c < a.length; c++)
            if (a[c] + "Transition"in b.style)
                return "-" + a[c].toLowerCase() + "-";
        return "transition"in b.style ? "" : !1
    }
    a.fn.removeStyle = function(b) {
        return this.each(function() {
            var h = a(this);
            b = b.replace(/\s+/g, "");
            var c = b.split(",");
            a.each(c, function() {
                var a = RegExp(this.toString() + "[^;]+;?", "g");
                h.attr("style", function(b, c) {
                    if (c)
                        return c.replace(a, "")
                })
            })
        })
    };
    var t = function(b) {
        return this.each(function() {
            function n(a, b) {
                function j() {
                    f.eq(a).removeStyle("opacity, z-index");
                    f.eq(b).removeStyle(h + "transition, transition");
                    k = b;
                    p = l=!1;
                    q = setTimeout(function() {
                        c("next")
                    }, d.slideDur);
                    "function" == typeof d.onFadeEnd && d.onFadeEnd.call(this, f.eq(k))
                }
                if (l || a == b)
                    return !1;
                l=!0;
                "function" == typeof d.onFadeStart&&!p && d.onFadeStart.call(this, f.eq(e));
                r.removeClass("active").eq(e).addClass("active");
                f.eq(a).css("z-index", 2);
                f.eq(b).css("z-index", 3);
                if (h) {
                    var g = {};
                    g[h + "transition"] = "opacity " + d.fadeDur + "ms";
                    g.opacity = 1;
                    f.eq(b).css(g);
                    setTimeout(function() {
                        j()
                    }, d.fadeDur)
                } else
                    f.eq(b).animate({
                        opacity: 1
                    },
                    d.fadeDur, function() {
                        j()
                    })
            }
            function c(a) {
                "next" == a ? (e = k + 1, e > m-1 && (e = 0)) : "prev" == a ? (e = k-1, 0 > e && (e = m-1)) : e = a;
                n(k, e)
            }
            var d = {
                slideDur: 7E3,
                fadeDur: 800,
                onFadeStart: null,
                onFadeEnd: null
            };
            b && a.extend(d, b);
            this.config = d;
            var j = a(this), l=!1, p=!0, q, k, e, f = j.find(".slide"), m = f.length, s = j.find(".pager_list");
            h = a.support.leadingWhitespace ? h(j[0]) : !1;
            for (var g = 0; g < m; g++)
                s.append('<li class="page" data-target="' + g + '">' + g + "</li>");
            j.find(".page").bind("click", function() {
                var b = a(this).attr("data-target");
                clearTimeout(q);
                c(b)
            });
            var r = s.find(".page");
            r.eq(0).addClass("active");
            n(1, 0)
        })
    };
    a.fn.easyFader = function(a) {
        return t.apply(this, arguments)
    }
})(jQuery);

/* --- EXTERNAL FUNCTIONS --- */

// IMG LOADED

function imgLoaded(img) {
    var $img = $(img);
    $img.closest('.img_wrapper').addClass('loaded');
};

// ASSET LOADED

function assetLoaded(asset) {
    if (typeof $ss === 'undefined')
        $ss = $('#HomeSlideshow');

    var $asset = $(asset),
    noAssets = $ss.find('img').length;

    $asset.addClass('loaded');
    var totLoaded = $ss.find('img.loaded').length;

    if (totLoaded == noAssets) {
        var $titles = $('#HomeSlideshow').find('.titles'),
        barTimer;

        $('#HomeSlideshow').easyFader({
            slideDur: 9200,
            fadeDur: 1200,
            onFadeStart: function() {
                $titles.removeClass('anim500').animate({
                    opacity: 0
                }, 400, function() {
                    $titles.removeClass('loaded').removeAttr('style');
                    $titles.find('.bar').removeAttr('style');
                });
            },
            onFadeEnd: function($slide) {
                var title = $slide.attr('data-title'),
                subtitle = $slide.attr('data-subtitle'),
                href = $slide.attr('data-href');

                $titles.find('h4').text(subtitle);
                $titles.find('h2 a').text(title).attr('href', href);
                $titles.addClass('anim500 loaded');

                if ($('#HomeSlideshow').find('.slide').length <= 1) {
                    return false;
                };

                if (!touch) {
                    if (typeof barTimer != 'undefined')
                        clearInterval(barTimer);
                    var barWidth = 0;

                    barTimer = setInterval(function() {
                        barWidth = barWidth + 0.22;
                        if (barWidth <= 100) {
                            $titles.find('.bar').css('width', barWidth + '%');
                        } else {
                            $titles.find('.bar').css('width', '100%');
                            clearInterval(barTimer);
                            $('#HomeSlideshow').find('.page.forward').click();
                        };
                    }, 10);
                };
            }
        });
    };
}
