let url = ''
/* if (__DEV__) {
 *   url = 'http://114.215.221.229/'
 * }
 * if (__PROD__) {*/
  url = 'https://remotex.ooclab.org/'
/* }*/

export const rootPath = url

export const errHandler = (e) => {
  // alert('[ XHR:Failed ] 详情请看控制台')
  console.error(e)
}
