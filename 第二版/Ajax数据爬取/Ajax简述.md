# Ajax
Asynchronous JavaScript and XML 异步的JavaScript和XML 

保证页面不被刷新，页面链接不改变的情况下与服务器交换数据并更新部分网页端技术

## 基本原理
初步了解了 Ajax 之后，我们再来详细了解它的基本原理。发送 Ajax 请求到网页更新的这个过程可以简单分为以下 3 步：

* 发送请求
* 解析内容
* 渲染网页

下面我们分别来详细介绍一下这几个过程。

#### 发送请求

我们知道 JavaScript 可以实现页面的各种交互功能，Ajax 也不例外，它也是由 JavaScript 实现的，实际上执行了如下代码：

```js
var xmlhttp;
if (window.XMLHttpRequest) {
    //code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();} else {//code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
xmlhttp.onreadystatechange=function() {if (xmlhttp.readyState==4 && xmlhttp.status==200) {document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
}
xmlhttp.open("POST","/ajax/",true);
xmlhttp.send();
```

这是 JavaScript 对 Ajax 最底层的实现，实际上就是新建了 XMLHttpRequest 对象，然后调用 onreadystatechange 属性设置了监听，然后调用 open() 和 send() 方法向某个链接（也就是服务器）发送了请求。前面用 Python 实现请求发送之后，可以得到响应结果，但这里请求的发送变成 JavaScript 来完成。由于设置了监听，所以当服务器返回响应时，onreadystatechange 对应的方法便会被触发，然后在这个方法里面解析响应内容即可。

#### 解析内容

得到响应之后，onreadystatechange 属性对应的方法便会被触发，此时利用 xmlhttp 的 responseText 属性便可取到响应内容。这类似于 Python 中利用 requests 向服务器发起请求，然后得到响应的过程。那么返回内容可能是 HTML，可能是 JSON，接下来只需要在方法中用 JavaScript 进一步处理即可。比如，如果是 JSON 的话，可以进行解析和转化。

#### 渲染网页

JavaScript 有改变网页内容的能力，解析完响应内容之后，就可以调用 JavaScript 来针对解析完的内容对网页进行下一步处理了。比如，通过 document.getElementById().innerHTML 这样的操作，便可以对某个元素内的源代码进行更改，这样网页显示的内容就改变了，这样的操作也被称作 DOM 操作，即对 Document 网页文档进行操作，如更改、删除等。

上例中，`document.getElementById("myDiv").innerHTML=xmlhttp.responseText` 便将 ID 为 myDiv 的节点内部的 HTML 代码更改为服务器返回的内容，这样 myDiv 元素内部便会呈现出服务器返回的新数据，网页的部分内容看上去就更新了。

我们观察到，这 3 个步骤其实都是由 JavaScript 完成的，它完成了整个请求、解析和渲染的过程。

再回想微博的下拉刷新，这其实就是 JavaScript 向服务器发送了一个 Ajax 请求，然后获取新的微博数据，将其解析，并将其渲染在网页中。
