import React, { Component } from 'react'
import numeral from 'numeral'
import moment from 'moment'
require('moment/locale/zh-cn')



export default class Item extends Component {
  render() {
    const {
      props: {
        data: {
          title,
          price,
          categories,
          abstract,
          release_date,
          view_count,
          url
        }
      }
    } = this

    return (
      <a href={url} target="_blank">
      <div className="r-item-panel">
        <div className="r-item-head">
          <h3 className="r-item-title">
            {title}
          </h3>
          <span className="r-item-price">
            &yen;&nbsp;{numeral(price).format('0,0')}
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
            {abstract}...
            <a className="r-item-link" href={url} target="_blank">
              &nbsp;查看更多
            </a>
          </p>

        </div>
        <div className="r-item-foot">
          <ul className="r-item-more">
            <li>{moment(release_date).startOf('day').fromNow()}发布</li>
            <li>{view_count}次浏览</li>
          </ul>
        </div>
        </div>
        </a>
    )
  }

}
