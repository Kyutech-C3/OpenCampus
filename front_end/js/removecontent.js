$(function(){
		/* worksクラスを持つ要素に対して処理  */
		$('.gotoPlayWindow').each(function(){
			// スマホやタブレットの場合
			if(isSmartPhone2()){
				$('.gotoPlayWindow').remove();
			}
		});
});
