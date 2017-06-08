import React, { Component } from 'react'
import _ from 'lodash'

export default class Pagination extends Component {
  constructor (props) {
    super(props)
  }

  action(page) {
    this.props.getAll(10, page)
  }

  render () {
    const {
      props: {
        filter: {
          current_page,
          page_size
        },
        total
      }
    } = this
    console.log(total / page_size)
    let sum = Math.ceil(total / page_size) || 0
    let next = current_page == sum ? false : current_page + 1
    let prev = current_page == 1 ? false : current_page - 1
    let firstPage = current_page - 2 >= 1 ? current_page - 2 : 1
    let lastPage = current_page <= 3 ?
                  6 :
                   (current_page + 3 >= sum ? sum : current_page + 3)
    
    return (
      <div className="r-pagination-warp">
      <ul className="r-pagination">
      {
        prev ?
        <li onClick={()=>{this.action(prev)}}>&lt;</li> :
                    <noscript />
      }
      {
        _.range(firstPage, lastPage).map((i, k) => {
          return (
            <li
            className={i != current_page || 'r-active'}
            onClick={() => {this.action(i)}}
            >
            {i}
            </li>
          )
        })
      }
      {
        next ?
        <li onClick={()=>{this.action(next)}}>&gt;</li> :
                    <noscript />
      }
      </ul>
      </div>
    )
  }
}
