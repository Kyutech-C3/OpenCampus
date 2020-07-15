$(function () {
  function resize_vrm_canvas(e) {
    const container = document.querySelector(".vrm_container");
    const width = container.clientWidth;
    const height = container.clientHeight;
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(width, height);
    camera.aspect = width/height;
    camera.updateProjectionMatrix();
  }
  window.addEventListener('resize', resize_vrm_canvas)
  // renderer
  const canvas = document.querySelector("#vrm_canvas");
  console.log(canvas.dataset.vrmUrl);
  console.log(canvas.clientWidth);
  const renderer = new THREE.WebGLRenderer({
    canvas: canvas,
    alpha: true
  });
  renderer.setClearColor(0x000000, 0);

  renderer.setSize( canvas.clientWidth, canvas.clientHeight );
  renderer.setPixelRatio( window.devicePixelRatio );

  // camera
  const camera = new THREE.PerspectiveCamera( 30.0, window.innerWidth / window.innerHeight, 0.1, 20.0 );
  camera.position.set( 0.0, 1.0, 5.0 );

  // camera controls
  const controls = new THREE.OrbitControls( camera, renderer.domElement );
  controls.screenSpacePanning = true;
  controls.target.set( 0.0, 1.0, 0.0 );
  controls.update();

  // scene
  const scene = new THREE.Scene();

  // light
  const light = new THREE.DirectionalLight( 0xffffff );
  light.position.set( 1.0, 1.0, 1.0 ).normalize();
  scene.add( light );

  // gltf and vrm
  const loader = new THREE.GLTFLoader();
  loader.crossOrigin = 'anonymous';
  loader.load(

      // URL of the VRM you want to load
    canvas.dataset.vrmUrl,

      // called when the resource is loaded
      ( gltf ) => {

          // calling this function greatly improves the performance
          THREE.VRMUtils.removeUnnecessaryJoints( gltf.scene );

          // generate VRM instance from gltf
          THREE.VRM.from( gltf ).then( ( vrm ) => {

              console.log( vrm );
              scene.add( vrm.scene );

              vrm.humanoid.getBoneNode( THREE.VRMSchema.HumanoidBoneName.Hips ).rotation.y = Math.PI;

          } );

      },

      // called while loading is progressing
      ( progress ) => console.log( 'Loading model...', 100.0 * ( progress.loaded / progress.total ), '%' ),

      // called when loading has errors
      ( error ) => console.error( error )

  );

  // helpers
  const gridHelper = new THREE.GridHelper( 10, 10 );
  scene.add( gridHelper );

  function animate() {

      requestAnimationFrame( animate );

      renderer.render( scene, camera );

  }

  animate();
  resize_vrm_canvas();
});
