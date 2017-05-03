import React, { Component } from 'react'


export default class Item extends Component {
  render() {
    const {
      props: {
        data: {
          title,
          price,
          categories
        }
      }
    } = this

    return (
      <div className="r-item-panel">
        <div className="r-item-head">
          <h3 className="r-item-title">
            {title}
          </h3>
          <span className="r-item-price">
            &yen;&nbsp;{price}
          </span>
        </div>
        <div className="r-item-body">
          <ul className="r-tags">
            {
              categories.map((i, k) => {
                return (
                  <li>{i.name}</li>
                )
              })
            }
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
            <li>{this.props.data['view_count']}次浏览</li>
          </ul>
        </div>
      </div>
    )
  }

}
