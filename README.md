# Interactive HTML BOM plugin for KiCad
# KiCad 交互式HTML BOM生成插件
![icon](https://i.imgur.com/js4kDOn.png)

This plugin generates convenient BOM listing with ability to visually correlate
and easily search for components and their placements on the pcb.
这个插件用于生成非常方便美观的BOM列表，并具有视觉关联的能力，容易搜索零件以及
在PCB上的摆放位置

This is really useful when hand soldering your prototype and you have to find 50
places where 0.1uF cap should be or which of the SOP8 footprints are for the same
micro. Dynamically highlighting all components in the same group on the rendering
of the pcb makes manually populating the board much easier.
这将使手动焊接PCB板变得更加容易。，例如当你需要找到50个0.1uF的电容的位置，
又或着在同样的SOP8丝印中区分不同零件。HTML BOM就可以突出显示同一组中的所有组件的数量

This plugin utilizes Pcbnew python bindings to read pcb data and render
silkscreen, fab layer, footprint pads, text and drawings. Additionally it can
pull data from schematic if you export it through netlist or xml file that
Eeschema can generate from it's internal bom tool. That extra data can be added
as additional columns in the BOM table (for example manufacturer id) or it can be
used to indicate which components should be omitted altogether (dnp field).
这个插件利用Pcbnew python绑定来读取pcb数据并呈现丝印层，制作层，脚印垫，文字和图纸。
另外它可以通过netlist或xml文件导出原理图中的数据
Eeschema可以从它的内部bom工具生成，并且可以添加额外的数据，
例如BOM表中的附加列(例如：制造商id)，或者可以用于指示哪些部件应该被完全省略(dnp字段)

 For
full description of functionality see [wiki](https://github.com/openscopeproject/InteractiveHtmlBom/wiki).
更多的描述请参考（只有英文） [wiki](https://github.com/openscopeproject/InteractiveHtmlBom/wiki).

Generated html page is fully self contained, doesn't need internet connection to work
and can be packaged with documentation of your project or hosted anywhere on the web.
生成的html页面是完全可以离线运行，不需要互联网
可以与项目文档打包在一起，也可以托管在网页上的任何位置。

[Demo is worth a thousand words.](https://openscopeproject.org/InteractiveHtmlBomDemo/)
[演示胜过千言万语]：(https://openscopeproject.org/InteractiveHtmlBomDemo/)

## Installation and Usage
## 安装与使用

See [project wiki](https://github.com/openscopeproject/InteractiveHtmlBom/wiki) for instructions.
更多详情请参考（只有英文： [项目WIKI](https://github.com/openscopeproject/InteractiveHtmlBom/wiki)

## License and credits
## 使用条款

Plugin code is licensed under MIT license, see `LICENSE` for more info.
插件代码被MIT开源协议保护, 更多详情请参考 `LICENSE` 

Html page uses [Split.js](https://github.com/nathancahill/Split.js),
[PEP.js](https://github.com/jquery/PEP) and (stripped down)
[lz-string.js](https://github.com/pieroxy/lz-string) libraries that get embedded into
generated bom page.
Html 页面使用了 [Split.js](https://github.com/nathancahill/Split.js),
[PEP.js](https://github.com/jquery/PEP) 和 (精简)
[lz-string.js](https://github.com/pieroxy/lz-string) 库，嵌入到已生成的bom页面.

`units.py` is borrowed from [KiBom](https://github.com/SchrodingersGat/KiBoM)
plugin (MIT license).
`units.py` 参考于 [KiBom](https://github.com/SchrodingersGat/KiBoM)
插件 (MIT协议).

`svgpath.py` is heavily based on
[svgpathtools](https://github.com/mathandy/svgpathtools) module (MIT license).
`svgpath.py` 大致上基于
[svgpathtools](https://github.com/mathandy/svgpathtools) 模块 (MIT 协议).
