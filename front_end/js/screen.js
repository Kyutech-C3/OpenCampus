window.onload = function(){
  var target = document.getElementById("embed");
  console.log(target);
  var btn    = document.getElementById("fullscreenSwitch");
  btn.onclick = requestFullscreen;
  /*フルスクリーン実行用ファンクション*/
  function requestFullscreen() {
  	if (target.webkitRequestFullscreen) {
  		target.webkitRequestFullscreen(); //Chrome15+, Safari5.1+, Opera15+
  	} else if (target.mozRequestFullScreen) {
  		target.mozRequestFullScreen(); //FF10+
  	} else if (target.msRequestFullscreen) {
  		target.msRequestFullscreen(); //IE11+
  	} else if (target.requestFullscreen) {
  		target.requestFullscreen(); // HTML5 Fullscreen API仕様
  	} else {
  		alert('ご利用のブラウザはフルスクリーン操作に対応していません');
  		return;
  	}
  	/*フルスクリーン終了用ファンクションボタンに切り替える*/
  	// btn.onclick = exitFullscreen;
  	// btn.innerText = "フルスクリーンを終了する";
  }
  /*フルスクリーン終了用ファンクション*/
  // function exitFullscreen() {
  // 	if (document.webkitCancelFullScreen) {
  // 		document.webkitCancelFullScreen(); //Chrome15+, Safari5.1+, Opera15+
  // 	} else if (document.mozCancelFullScreen) {
  // 		document.mozCancelFullScreen(); //FF10+
  // 	} else if (document.msExitFullscreen) {
  // 		document.msExitFullscreen(); //IE11+
  // 	} else if(document.cancelFullScreen) {
  // 		document.cancelFullScreen(); //Gecko:FullScreenAPI仕様
  // 	} else if(document.exitFullscreen) {
  // 		document.exitFullscreen(); // HTML5 Fullscreen API仕様
  // 	}
  // 	/*フルスクリーン実行用ファンクションボタンに切り替える*/
  // 	btn.onclick = requestFullscreen;
  // 	btn.innerText = "フルスクリーンにする";
  // }
  // /*サポートしていないIE10以下とスマフォではフルスクリーンボタンを非表示*/
  if(typeof window.orientation != "undefined" || (document.uniqueID && document.documentMode < 11)){
  	btn.style.display = "none";
  }
    btn.onclick = requestFullscreen;
}
