// url：string，请求的地址
// query：object，请求携带的参数
// callback：function，成功之后回调
// isJson：boolean，是否需要解析json
const utils = {
    get: function (url, query, callback, isJson) {
        // 如果有参数，先把参数拼接在url后面
        if (query) {
            url += '?';
            for (let key in query) {
                url += `${key}=${query[key]}&`;
            }
            // 取出最后多余的&
            url = url.slice(0, -1);
        }

        let xhr = new XMLHttpRequest();
        xhr.open("get", url, true);
        xhr.send();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    if (isJson === true) {
                        resp = JSON.parse(xhr.responseText);
                    } else {
                        resp = xhr.responseText;
                    }
                    callback(resp);
                }
            }
        }
    },
    post: function (url, query, callback, isJson) {
        // 如果有参数，先把参数拼接
        let val = '';
        if (query) {
            for (let key in query) {
                val += `${key}=${query[key]}&`;
            }
            // 取出最后多余的&
            val = val.slice(0, -1);
        }

        let xhr = new XMLHttpRequest();
        xhr.open("post", url, true);
        xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
        xhr.send(val);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    if (isJson === true) {
                        resp = JSON.parse(xhr.responseText);
                    } else {
                        resp = xhr.responseText;
                    }
                    callback(resp);
                }
            }
        }
    },
    // params:object   {method, url, query, callback, isJson}
    ajax: function (params) {
        let xhr = new XMLHttpRequest();

        if (params.method.toLowerCase() === "get") {
            if (params.query) {
                params.url += '?';
                for (let key in params.query) {
                    params.url += `${key}=${params.query[key]}&`;
                }
                // 取出最后多余的&
                params.url = params.url.slice(0, -1);
            }
            xhr.open("get", params.url);
            xhr.send()
        } else {
            // post请求
            let val = '';
            if (params.query) {
                for (let key in params.query) {
                    val += `${key}=${params.query[key]}&`;
                }
                // 取出最后多余的&
                val = val.slice(0, -1);
            }
            xhr.open("post", params.url);
            xhr.setRequestHeader("content-type", "application/x-www-form-urlencoded");
            xhr.send(val)
        }
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    let resp = params.isJson ? JSON.parse(xhr.responseText) : xhr.responseText;
                    params.callback(resp);
                }
            }
        }
    },
    // 基于promise的get请求
    fetch: function (url, query, isJson) {
        if (query) {
            url += '?';
            for (let key in query) {
                url += `${key}=${query[key]}&`;
            }
            // 取出最后多余的&
            url = url.slice(0, -1);
        }
        return new Promise(function (resolve, reject) {
            let xhr = new XMLHttpRequest();
            xhr.open("get", url, true);
            xhr.send();
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        let resp = isJson ? JSON.parse(xhr.responseText) : xhr.responseText;
                        resolve(resp);
                    }else {
                        reject();
                    }
                }
            }
        })
    }
};