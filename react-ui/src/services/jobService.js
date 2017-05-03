import xhr from './xhr/'

class JobService {

  fetch () {
    const url = `/api/jobx/job`
    return xhr({ url })
  }

}

// 实例化后再导出
export default new JobService()
