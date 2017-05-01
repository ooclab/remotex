import React, { Component } from 'react'

export default class Pagination extends Component {
  constructor (props) {
    super(props)
  }

  render () {
    return (
      <div className="r-pagination-warp">
        <ul className="r-pagination">
          <li className="r-active">1</li>
          <li>2</li>
          <li>3</li>
        </ul>
      </div>
      
    )
  }
}
