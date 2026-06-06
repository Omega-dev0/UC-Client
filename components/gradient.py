from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import RenderContext
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.graphics import RenderContext, Color, Rectangle

# GLSL Shader Code - Transféré du CSS à un shader par IA parce que je vais pas le faire à la main
SHADER = """
$HEADER$
uniform vec2 u_resolution;

void main(void) {
    // Use local rectangle UVs so the gradient always fills the full widget.
    vec2 uv = tex_coord0.xy;
    
    // 1. Base Linear Gradient (180deg: Top to Bottom)
    vec3 topColor = vec3(0.984, 1.0, 0.984);   
    vec3 bottomColor = vec3(0.933, 0.976, 0.941); 
    vec3 baseLinear = mix(bottomColor, topColor, uv.y);
    
    // 2. Upper radial gradient (shifted toward top-center)
    vec2 topLeftCenter = vec2(0.14, 0.12);
    float distToTopLeft = distance(uv, topLeftCenter);
    float radial1Alpha = smoothstep(0.40, 0.0, distToTopLeft) * 0.24;
    vec3 radial1Color = vec3(0.357, 0.749, 0.357);
    vec3 colorMix1 = mix(baseLinear, radial1Color, radial1Alpha);
    
    // 3. Upper radial gradient (shifted toward top-center)
    vec2 topRightCenter = vec2(0.88, 0.32);
    float distToTopRight = distance(uv, topRightCenter);
    float radial2Alpha = smoothstep(0.38, 0.0, distToTopRight) * 0.76;
    vec3 radial2Color = vec3(1.0, 0.796, 0.894);
    
    vec3 finalColor = mix(colorMix1, radial2Color, radial2Alpha);
    
    gl_FragColor = vec4(finalColor, 1.0);
}
"""


class GradientBackground(Widget):
    def __init__(self, **kwargs):
        self.canvas = RenderContext(
            use_parent_projection=True,
            use_parent_modelview=True,
            use_parent_frag_modelview=True,
        )
        super().__init__(**kwargs)
        self.canvas.shader.fs = SHADER

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_shader, pos=self.update_shader)
        self.update_shader()

    def update_shader(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.canvas["u_resolution"] = [float(n) for n in self.size]
