// PV Tool — Copyright (c) 2026 DanteAlighieri13210914
// Licensed under Non-Commercial License. See LICENSE for terms.

import { Filter, GlProgram } from 'pixi.js';

const vertex = `
in vec2 aPosition;
out vec2 vTextureCoord;
uniform vec4 uInputSize;
uniform vec4 uOutputFrame;
uniform vec4 uOutputTexture;

void main(void) {
  vec2 position = aPosition * uOutputFrame.zw + uOutputFrame.xy;
  position.x = position.x * (2.0 / uOutputTexture.x) - 1.0;
  position.y = position.y * (2.0 * uOutputTexture.z / uOutputTexture.y) - uOutputTexture.z;
  gl_Position = vec4(position, 0.0, 1.0);
  vTextureCoord = aPosition * (uOutputFrame.zw * uInputSize.zw);
}
`;

const fragment = `
in vec2 vTextureCoord;
uniform sampler2D uTexture;
uniform float uIntensity;
uniform float uTime;

float hash(vec2 p) {
  return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453);
}

void main(void) {
  vec2 uv = vTextureCoord;
  float intensity = uIntensity;

  // Block displacement: divide into horizontal bands, randomly offset some
  float bandHeight = 0.02 + intensity * 0.06;
  float bandIdx = floor(uv.y / bandHeight);
  float bandNoise = hash(vec2(bandIdx, floor(uTime * 6.0)));

  vec2 dispUV = uv;
  if (bandNoise > 1.0 - intensity * 0.4) {
    float shift = (hash(vec2(bandIdx + 0.5, floor(uTime * 8.0))) - 0.5) * intensity * 0.12;
    dispUV.x += shift;
  }

  // Chromatic aberration: offset R and B channels horizontally
  float rgbOffset = intensity * 0.008;
  float r = texture2D(uTexture, vec2(dispUV.x + rgbOffset, dispUV.y)).r;
  float g = texture2D(uTexture, dispUV).g;
  float b = texture2D(uTexture, vec2(dispUV.x - rgbOffset, dispUV.y)).b;
  float a = texture2D(uTexture, dispUV).a;

  gl_FragColor = vec4(r, g, b, a);
}
`;

export class GlitchFilter extends Filter {
  constructor() {
    const glProgram = new GlProgram({ fragment, vertex, name: 'glitch-filter' });
    super({
      glProgram,
      resources: {
        glitchUniforms: {
          uIntensity: { value: 0.0, type: 'f32' },
          uTime: { value: 0.0, type: 'f32' },
        },
      },
    });
  }

  set intensity(value: number) {
    this.resources.glitchUniforms.uniforms.uIntensity = value;
  }

  get intensity(): number {
    return this.resources.glitchUniforms.uniforms.uIntensity;
  }

  set time(value: number) {
    this.resources.glitchUniforms.uniforms.uTime = value;
  }
}