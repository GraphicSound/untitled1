/**
 * Created by yu on 12/15/14.
 */
var isTransition = false; // 动画标记，防止滑动事件叠加
var isGalleryGenerated = false; // gallery已经生成的标志，因为这玩意儿不能重复生成！！！

$(document).ready(function() {

    // 在整个窗口绑定鼠标滑动事件
    $('body').on('mousewheel DOMMouseScroll', doScroll);
    // 内部滑动
    $('#inner-content-div').slimScroll({
        height: '100%'
    });

    // 看来只有曲线救国了
    $('#inner-content-div').hover(function() {
        $('body').off('mousewheel DOMMouseScroll', doScroll);
    }, function() {
        $('body').on('mousewheel DOMMouseScroll', doScroll);
    });

    //  // 内部滑动事件
    //  $('.section-footer').mousewheel(function(event, delta) {
    //      console.log("内部滑动");
    //      // 内部滑动
    //      return false; // prevent default
    //  });

    //  // 取消section-footer对doScroll滑动事件的监听 // 后来发现其实不用取消，直接再绑定，但是必须prevent default
    //  $('.section-footer').off('mousewheel DOMMouseScroll', doScroll);
    //  $('.section-footer').off('mousewheel DOMMouseScroll');
    //  $('.section-footer').off();

    // 添加属性
    $('#panels').children().each(function(index) {
        $(this).attr("data-index", index+1);
        $(this).css({"position" : "absolute", "top" : (index*100 + "%")});
    });

    // 添加检测panels动画结束的事件，延迟一秒钟，这样停顿感更强
    $('#panels').on('transitionend webkitTransitionEnd oTransitionEnd MSTransitionEnd', function(e){
        // access original Event object versus jQuery's normalized version
        setTimeout(function(){
            isTransition = false;
        }, 1000);
    });

    // header_panel
    // active第一个分页
    $('#header_panel').addClass("active");

    // 绑定点击事件
    $('.glyphicon-chevron-down').click(function() {
        scrollDown();
    });

    // features_panel
    // active第一个分页
    $('.features-themes').addClass("active");
    // 显示条添加left属性

    $('.feature-tag').css({'left' : '115px'});
    // 绑定点击事件
    $('#features_panel .section-header').click(function(event) {
        var element = $(event.target);
        var parentClass = element.parent().attr('class');
        if(parentClass.indexOf("active") >= 0) { // jQuery里面检测字符串包含
            // 如果已经是选中的，直接跳出
            // alert("active");
            return;
        }

        // 遍历features_panel查找对顶点击的对象
        $('.features').children().each(function(index) {
            if($(this).attr('class') == parentClass) {
                // alert(index);
                // 取消之前高亮显示
                var activeFeature = $('.feature.active'); // 这个同时也会取消下面footer的active，因为他们的class是一样的
                activeFeature.removeClass('active');
                // 增加高亮显示
                $(this).addClass('active');
                // 将显示条移动到高亮对象下面
                $('.feature-tag').css({'left' : (115 + index*147) + 'px'});

                // 利用index，将footer对应的内容显示出来
                $('.features-detail').children().each(function(i) { // 暂时不知道除了遍历更好的办法
                    if(index == i) {
                        $(this).addClass('active');
                    }
                });
            }
        });
    });
});

var doScroll = function(event) {
    // 如果已经在动画，直接返回
    if (true == isTransition) return;

    if (event.originalEvent.wheelDelta > 0 || event.originalEvent.detail < 0) {
        // scroll up
        // alert("scroll up");
        scrollUp();
    } else {
        // scroll down
        // alert("scroll down");
        scrollDown();
    }

    return false; // prevent default
};

var scrollUp = function() {
    var activeElement = $('.section.active'); // 记住要连着写
    var dataIndex = parseInt(activeElement.attr("data-index")); // 要先parseInt，不然之后相加始终都是字符串相加

    if(1 == dataIndex) return;
    activeElement.removeClass("active");
    var nextActive = $("[data-index='" + (dataIndex-1) + "']");
    nextActive.addClass("active");

    isTransition = true;
    $('#panels').css({"position": "relative", "transform": "translate3d(0px, -" + (dataIndex-2)*100 + "%, 0px)", "transition": "all 600ms ease 0s"});
};

var scrollDown = function() {
    var activeElement = $('.section.active'); // 记住要连着写
    var dataIndex = parseInt(activeElement.attr("data-index")); // 要先parseInt，不然之后相加始终都是字符串相加

    if(1 == dataIndex) {
        return;
    }
    activeElement.removeClass("active");
    var nextActive = $("[data-index='" + (dataIndex+1) + "']");
    nextActive.addClass("active");

    isTransition = true;
    $('#panels').css({"position": "relative", "transform": "translate3d(0px, -" + (dataIndex)*100 + "%, 0px)", "transition": "all 600ms ease 0s"});
};
