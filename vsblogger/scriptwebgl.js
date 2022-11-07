
    const canvas = window.canvas;const gl = canvas.getContext("webgl2");const dpr = Math.max(1, window.devicePixelRatio);
   //            <canvas id="canvas" width="1921" height="485"></canvas>
    const vertexSource = `#version 300 es
    #ifdef GL_FRAGMENT_PRECISION_HIGH
    precision highp float;
    #else
    precision mediump float;
    #endif
    in vec2 position;void main(void) { gl_Position = vec4(position, 0., 1.);}`;
    const fragmentSource = `#version 300 es
    #ifdef GL_FRAGMENT_PRECISION_HIGH
    precision highp float;
    #else
    precision mediump float;
    #endif
    out vec4 fragColor;uniform vec2 resolution;uniform float time;
    #define T time
    vec3 pn(vec2 uv) { for (int i = 0; i < 100; i++) { vec2 p = vec2(  cos(uv.y + T/3.8 ),   sin(uv.x +  T/3.8 )  ) ;p +=0.3; uv.xy += p;   }
      float  r = sin(uv.x -0.5) * 2.5 , b = sin(uv.y +0.5) * 0.5 + 0.5, g = sin((uv.x + uv.y ) * 2.5) * 4.5 + 0.5; return vec3(r, g, b);}
    void main() {	vec2 uv = (gl_FragCoord.xy - 0.5 * resolution.xy) / resolution.y;float f = cos(T * 0.2) +4.0;
    float zoom =3.2* f;uv *= zoom;vec2 gv = fract(uv * zoom) - 0.5;float mm = cos(T);
    
    vec3 col = vec3(1.8); vec3 st = pn(uv);float r =22.2* col.z,g = min(st.b, .5 * (-mm+ 1.5) * col.x),b = min(st.g * 2.1, .5 * (1. -mm) * col.y), a = 1.;
    fragColor =vec4(vec3(g) - st, a) * 4.;}  `;let time;let buffer;let program;let resolution;let vertices = [];
    function resize() { const { innerWidth: width, innerHeight: height } = window;
    canvas.width = width * dpr; canvas.height = height * dpr;
    gl.viewport(0, 0, width * dpr, height * dpr);}
    function compile(shader, source) { gl.shaderSource(shader, source); gl.compileShader(shader);
     if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {   console.error(gl.getShaderInfoLog(shader)); }}
    
    function setup() { const vs = gl.createShader(gl.VERTEX_SHADER);
      const fs = gl.createShader(gl.FRAGMENT_SHADER);
    
      program = gl.createProgram();
    
      compile(vs, vertexSource);
      compile(fs, fragmentSource);
    
      gl.attachShader(program, vs);
      gl.attachShader(program, fs);
      gl.linkProgram(program);
    
      if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {console.error(gl.getProgramInfoLog(program));}
    
      vertices = [-1.0, -1.0, 1.0, -1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0, 1.0];buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, "position"); gl.enableVertexAttribArray(position); gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
     time = gl.getUniformLocation(program, "time"); resolution = gl.getUniformLocation(program, "resolution");}
    
    function draw(now) { gl.clearColor(0, 0, 0, 1); gl.clear(gl.COLOR_BUFFER_BIT); gl.useProgram(program); gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
     gl.uniform1f(time, now * 0.001); gl.uniform2f(resolution, canvas.width, canvas.height); gl.drawArrays(gl.TRIANGLES, 0, vertices.length * 0.5);}
    function loop(now) {  draw(now); requestAnimationFrame(loop);}
    function init() { setup();  loop(0);}
    document.body.onload = init;window.onresize = resize;