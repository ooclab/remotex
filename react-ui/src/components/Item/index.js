import React, { Component } from 'react'


export default class Item extends Component {
  render() {
    return (
      <div className="r-item-panel">
        <div className="r-item-head">
          <h3 className="r-item-title">
            [远程] 短期项目 vuejs 前端(1 名) 和 Python (1-2 名) – 量化分析
          </h3>
          <span className="r-item-price">
            &yen;&nbsp;3,000
          </span>
        </div>
        <div className="r-item-body">
          <ul className="r-tags">
            <li>web</li>
            <li>招聘其实</li>
          </ul>
          <p className="r-item-detail">
            本人曾在美投行和全球 top3 对冲基金做量化分析，刚辞了职要自己 (在伦敦) 单干。现在在做一个实时的分析和交易系统，但如果我自己一个人做太累 (我还要陪女儿玩去 ;p), 所以想找大牛 boost 一下进度, 帮忙实现某些部分。
            <a className="r-item-link" href="javascript:;" target="_blank">
              查看更多
            </a>
          </p>

        </div>
        <div className="r-item-foot">
          <ul className="r-item-more">
            <li>1天前发布</li>
            <li>36次浏览</li>
          </ul>
        </div>
      </div>
    )
  }

}
