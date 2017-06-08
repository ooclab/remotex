import xhr from './xhr/'

class JobService {

  fetch (lm, p) {
    const url = `/api/jobx/job?lm=${lm}&p=${p}`
    return xhr({ url })
  }

}

// 实例化后再导出
export default new JobService()
