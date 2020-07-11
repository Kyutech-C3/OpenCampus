function toggleNav() {
  var body = document.body;
  var hamburger = document.getElementById('js-hamburger');
  var blackBg = document.getElementById('js-black-bg');
  // js-scroll-item というクラスのオブジェクトを全て取得（配列みたいな感じ）
  var scrollItems = document.getElementsByClassName('js-scroll-item');
  /* js-hamburger（ハンバーガーの3本線のアイコン）クリックで, body にnav-openクラスを付与  */
  hamburger.addEventListener('click', function() {
    body.classList.toggle('nav-open');
  });
  /* もう一度クリックすることでnav-openクラスを削除  */
  blackBg.addEventListener('click', function() {
    body.classList.remove('nav-open');
  });

  // 配列変数「scrollItmes」の要素数分ループ処理
  for(var $i = 0; $i < scrollItems.length; $i++ ) {
      // クリックイベントにイベントハンドラをバインド
      scrollItems[$i].onclick = function () {
        // class属性値が「js-scroll-item」である要素をクリックした時の処理
        body.classList.remove('nav-open');
      }
  }
}
toggleNav();
