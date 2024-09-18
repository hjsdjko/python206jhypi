const base = {
    get() {
        return {
            url : "http://localhost:8080/python206jhypi/",
            name: "python206jhypi",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "BS23-287基于Python的期货程序化交易系统的设计与实现"
        } 
    }
}
export default base
