// 画面サイズが600px以下の場合
function isSmartPhone() {
  if (window.matchMedia && window.matchMedia('(max-device-width: 600px)').matches) {
    return true;
  } else {
    return false;
  }
}


// スマホやタブレットを判定する
function isSmartPhone2() {
  var ua = navigator.userAgent;
  if (ua.indexOf('iPhone') > 0 || ua.indexOf('iPod') > 0 || ua.indexOf('Android') > 0 || ua.indexOf('Android') > 0 && ua.indexOf('Mobile') > 0) {
    return true;
  } else {
    return false;
  }
}

// function isSmartPhone2() {
//   if (navigator.userAgent.match(/iPhone|Android.+Mobile/)) {
//     return true;
//   } else {
//     return false;
//   }
// }
