// 画面サイズが600px以下の場合trueを返す(スマホと判定する)
function isSmartPhone() {
  if (window.matchMedia && window.matchMedia('(max-device-width: 600px)').matches) {
    return true;
  } else {
    return false;
  }
}
