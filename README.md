# 爬虫笔记

+ 使用selector ()方法时，复制的路径

  `li:nth-child(1)在运行中会报错，应该改为li:nth-of-type(1)`

+ 当提取的的内容如下

  ```[<i>898</i>]```

  这个时候使用get_text()方法就可以获得中间的文字信息。

+ 在使用selector()方法时，如果下一个标签是上一个标签的子标签，前面的相同路径可以省略。

+ 使用strip()方法可以去除换行符

+ 在使用re模块的时候，编写正则表达式时，注意其中的空格，如果空格不对将匹配不出来正确的结果 

+ 如果是在使用**lxml**库时提取标签中的信息则使用/text()方法。

+ 遇到相同类型的标签如

  ```<li class="tag-1">需要的内容1</li>
  <li class="tag-1">需要的内容1</li>
  <li class="tag-2">需要的内容2</li>
  <li class="tag-3">需要的内容3</li>
  ```


​        此时的代码应该这样写：`contents = selector.xpath('//li[starts-with(@class,"tag")]/text()')`



+ 当遇到标签套标签的时候可以通过string(.)方法完成。

