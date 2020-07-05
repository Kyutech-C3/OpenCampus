$(function(){
	$(window).scroll(function(){
		/* worksクラスを持つ要素に対して処理  */
		$('.works').each(function(){
			var elemPos = $(this).offset().top;	// ドキュメント上での表示位置（topのみ取得）
			var scroll = $(window).scrollTop();	// 現在のスクロール上の上位置を取得
			var windowHeight = $(window).height();	//ウインドウの高さをピクセル単位で取得
			var fadeinOffset;
			var fadeoutOffset = 400;

			if(scroll <= elemPos){
				$(this).addClass('up');
				$(this).removeClass('down');
			}
			else{
				$(this).addClass('down');
				$(this).removeClass('up');
			}
			// スマホの場合
			if(isSmartPhone()){
				fadeinOffset = 100;
			}
			else{
				fadeinOffset = 200;
			}
			// 画面内に入って200pxスクロールしたら
			if ((scroll > elemPos - windowHeight + fadeinOffset)){
				// scrollin クラスを追加
				$(this).addClass('scrollin');
				$(this).removeClass('scrollout');
			}
			else if((scroll < -elemPos + windowHeight + fadeoutOffset)){
				$(this).addClass('scrollout');
				$(this).removeClass('scrollin');
			}
			else{
				$(this).removeClass('scrollin');
				$(this).removeClass('scrollout');
			}
		});
	});
});
