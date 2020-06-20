$(function(){
	$(window).scroll(function(){
		/* fadeinクラスを持つ要素に対して処理  */
		$('.fadein').each(function(){
			var elemPos = $(this).offset().top;	// ドキュメント上での表示位置（場合topのみ取得）
			var scroll = $(window).scrollTop();	// 要素の現在のスクロール上の上位置を取得
			var windowHeight = $(window).height();	//ウインドウの高さをピクセル単位で取得
			// 画面内に入って200pxスクロールしたら
			if (scroll > elemPos - windowHeight + 200){
				// scrollin クラスを追加		
				$(this).addClass('scrollin');
			}
			else{
				$(this).removeClass('scrollin');
			}
		});
	});
});
