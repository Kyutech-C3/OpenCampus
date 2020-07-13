$(function(){
    /* global-nav__itemクラスを持つ要素に対して処理  */
    $('.global-nav__item').each(function(){
      // スマホやタブレットの場合
      if(isSmartPhone2()){
        $('.global-nav__item').remove();
      }
    });
});
