<template>
  <div id="app">
    <div v-if="showDetail">
      <router-view ></router-view>
      <mu-raised-button label="关闭详情" @click="closeDetailPopup" primary fullWidth/>
    </div>
    <div v-else id="home">
      <!-- part 1 顶部 -->
      <mu-appbar title="RemoteX 快乐工作 认真生活">

        <!-- 右侧抽屉按钮 -->
        <mu-icon-button slot="right" @click="toggleDrawer(true)">
          <img style="width:24px; height:24px;" src="./assets/more.png" />
        </mu-icon-button>
        
        <!-- Slack icon 
        <mu-icon-button slot="right" href="https://remotex.slack.com/shared_invite/MTcwMDMxOTA4MjA5LTE0OTI1MTM1NTctMjY5MjhmMGZmMQ" target="_blank">
          <img style="width:24px; height:24px;" src="./assets/Slack_White.png" />
        </mu-icon-button>--> 

        <!-- GitHub icon 
        <mu-icon-button slot="right" href="https://github.com/ooclab/remotex" target="_blank">
          <img style="width:24px; height:24px;" src="./assets/GitHub_White.png" />
        </mu-icon-button>-->
      </mu-appbar>

      <!-- part 1.1 抽屉 -->
      <mu-drawer right :open="openDrawer" :docked="docked" @close="toggleDrawer()">
        <mu-list @close="docked ? '' : toggleDrawer()">

          <!-- GitHub -->
          <mu-list-item title="GitHub" href="https://github.com/ooclab/remotex" target="_blank">
            <img style="width:24px; height:24px; position:absolute;left:15px;top:10px;" src="./assets/GitHub.png"/>
          </mu-list-item>

          <!-- Slack -->
          <mu-list-item title="Slack" href="https://remotex.slack.com/shared_invite/MTcwMDMxOTA4MjA5LTE0OTI1MTM1NTctMjY5MjhmMGZmMQ" target="_blank">
            <img style="width:24px; height:24px; position:absolute;left:15px;top:10px;" src="./assets/Slack.png"/>
          </mu-list-item>

          <!-- Redmine -->
          <mu-list-item title="Redmine" href="https://wp.ooclab.org/boards/1/topics/1" target="_blank">
            <img style="width:20px; height:20px; position:absolute;left:17px;top:12px;" src="./assets/assignment.png"/>
          </mu-list-item>
          <mu-divider/>

          <!-- 关于 -->
          <mu-list-item title="About" href="https://wp.ooclab.org/boards/1/topics/1" target="_blank">
            <img style="width:20px; height:20px; position:absolute;left:17px;top:12px;" src="./assets/info.png"/>
          </mu-list-item>

          <!-- 联系 -->
          <mu-list-item title="Contact" href="https://github.com/ooclab/remotex" target="_blank">
            <img style="width:20px; height:16px; position:absolute;left:17px;top:14px;" src="./assets/mail.png"/>
          </mu-list-item>
          <mu-divider/>

          <!-- 关闭 -->
          <mu-list-item @click.native="openDrawer = false" title="Close">
            <img style="width:16px; height:16px; position:absolute;left:19px;top:15px;" src="./assets/close.png"/>
          </mu-list-item>
        </mu-list>
      </mu-drawer>

      <!-- part 2 搜索栏 -->
      <div>

        <!-- 关键词输入框 -->
        <mu-text-field style="width:60%;" label="请输入关键词" labelFloat @change="textChanged"/>

        <!-- 搜索按钮 -->
        <mu-flat-button label="搜索" class="demo-flat-button" primary @click="search">
          <img style="width:18px; height:18px; margin-left:10px;" src="./assets/search.png" />
        </mu-flat-button>
      </div>

      <!-- part 3 类目栏 -->
      <div>
        <!-- 平台 -->
        <!--
        <mu-raised-button style="width:40%; margin: 5px 5px 5px 0;" @click="openBottomSheet1" :label="platformTitle" icon="assignment_turned_in"/>
        <mu-bottom-sheet :open="bottomSheet1" @close="closeBottomSheet1">
          <mu-list @itemClick="closeBottomSheet1()" style="height:200px">
            <mu-sub-header>
              请选择平台
            </mu-sub-header>
            <mu-list-item title="全部" @click="categoryItemClick('platform', '', '平台')"/>
            <mu-list-item title="外包众包" @click="categoryItemClick('platform', '码市', '外包众包')"/>
            <mu-list-item title="远程工作" @click="categoryItemClick('platform', '实现网', '远程工作')"/>
          </mu-list>
        </mu-bottom-sheet>
        -->

        <!-- 角色 -->
        <!--
        <mu-raised-button style="width:40%; margin: 5px 0 5px 5px;" @click="openBottomSheet2" :label="roleTitle" icon="build"/>
        <mu-bottom-sheet :open="bottomSheet2" @close="closeBottomSheet2">
          <mu-list @itemClick="closeBottomSheet2" style="height:240px">
            <mu-sub-header>
              请选择角色
            </mu-sub-header>
            <mu-list-item title="全部" @click="categoryItemClick('role', '0', '角色')"/>
            <mu-list-item title="项目管理" @click="categoryItemClick('role', '1', '项目管理')""/>
            <mu-list-item title="产品经理" @click="categoryItemClick('role', '2', '产品经理')"/>
            <mu-list-item title="设计" @click="categoryItemClick('role', '3', '设计')"/>
            <mu-list-item title="开发" @click="categoryItemClick('role', '4', '开发')"/>
            <mu-list-item title="测试" @click="categoryItemClick('role', '5', '测试')"/>
            <mu-list-item title="运维" @click="categoryItemClick('role', '6', '运维')"/>
            <mu-list-item title="市场" @click="categoryItemClick('role', '7', '市场')"/>
            <mu-list-item title="运营" @click="categoryItemClick('role', '8', '运营')"/>
          </mu-list>
        </mu-bottom-sheet>
        -->

        <!-- 工作 -->
        <!--
        <mu-raised-button style="width:40%; margin: 5px 5px 5px 0;" @click="openBottomSheet3" :label="workTitle" icon="devices"/>
        <mu-bottom-sheet :open="bottomSheet3" @close="closeBottomSheet3">
          <mu-list @itemClick="closeBottomSheet3" style="height:240px">
            <mu-sub-header>
              请选择工作
            </mu-sub-header>
            <mu-list-item title="全部" @click="categoryItemClick('work', '0', '工作')"/>
            <mu-list-item title="Web 页面" @click="categoryItemClick('work', '1', 'Web 页面')"/>
            <mu-list-item title="App 移动应用" @click="categoryItemClick('work', '2', 'App 移动应用')"/>
            <mu-list-item title="微信开发" @click="categoryItemClick('work', '3', '微信开发')"/>
            <mu-list-item title="咨询" @click="categoryItemClick('work', '4', '咨询')"/>
          </mu-list>
        </mu-bottom-sheet>
        -->

        <!-- 城市 -->
        <!--
        <mu-raised-button style="width:40%; margin: 5px 0 5px 5px;" @click="openBottomSheet4" :label="cityTitle" icon="location_city"/>
        <mu-bottom-sheet :open="bottomSheet4" @close="closeBottomSheet4">
          <mu-list @itemClick="closeBottomSheet4" style="height:240px">
            <mu-sub-header>
              请选择城市
            </mu-sub-header>
            <mu-list-item title="全部" @click="categoryItemClick('city', '', '城市')"/>
            <mu-list-item title="北京" @click="categoryItemClick('city', '北京', '北京')"/>
            <mu-list-item title="上海" @click="categoryItemClick('city', 'shanghai', '上海')"/>
            <mu-list-item title="广州" @click="categoryItemClick('city', '3', '广州')"/>
            <mu-list-item title="深圳" @click="categoryItemClick('city', '4', '深圳')"/>
            <mu-list-item title="杭州" @click="categoryItemClick('city', '5', '杭州')"/>
            <mu-list-item title="成都" @click="categoryItemClick('city', '6', '成都')"/>
            <mu-list-item title="武汉" @click="categoryItemClick('city', '7', '武汉')"/>
            <mu-list-item title="南京" @click="categoryItemClick('city', '8', '南京')"/>
            <mu-list-item title="西安" @click="categoryItemClick('city', '9', '西安')"/>
            <mu-list-item title="厦门" @click="categoryItemClick('city', '10', '厦门')"/>
            <mu-list-item title="其他" @click="categoryItemClick('city', '11', '其他')"/>
          </mu-list>
        </mu-bottom-sheet>
        -->
      </div>


      <!-- part 4 排序栏 -->
      <div>
        <!--<mu-tabs style="background:#424242;">-->
        <mu-tabs id="tabs" :value="activeTab" @change="sortItemClick">
          <mu-tab :id="sortTab1Style" value="release_date" title="最新发布"/>
          <mu-tab :id="sortTab2Style" value="view_count" title="热门机会"/>
          <mu-tab :id="sortTab3Style" value="price" title="高薪报酬"/>
        </mu-tabs>
      </div>

      <!-- part 5 列表栏 -->
      <div>
        <mu-list>

          <!-- 循环体 -->
          <template v-for="item in list" class="page-infinite-listitem">

            <!-- 卡片 -->
            <mu-card style="margin: 15px 20px 15px 20px; text-align: left;">
              

              <!-- 标题 / 来源 -->
              <a @click="openDetailPopup(item.id)" :href="item.url" target="_blank">
                <!--<mu-card-title :title="item.title" :subTitle="item.url"/>-->
                <mu-card-title :title="item.title" :subTitle="item.abstract"/>
              </a>

              <!-- tags -->
              <mu-card-actions v-if="item.categories" style="display: flex;">
                <template v-for="chip in item.chips">
                  <mu-chip style="margin-left: 5px;">
                    {{ chip.name }}
                  </mu-chip>
                </template>
              </mu-card-actions>

              <!-- 正文 -->
              <!--<mu-card-text>
                {{ item.body }}
              </mu-card-text>-->

              <!-- 价格 -->
              <a @click="openDetailPopup(item.id)" :href="item.url" target="_blank">
                <mu-card-actions style="display: flex;">
                  <p>报酬&nbsp;<b>{{ item.price }}</b></p>
                </mu-card-actions>
              </a>

              <!-- 其他 -->
              <a @click="openDetailPopup(item.id)" :href="item.url" target="_blank" style="font-size: 12px; color: #BDBDBD;">
                <mu-card-actions style="display: flex;">

                <!-- 暂无用户注册及评论功能
                  <mu-flat-button :label="item.vote_up" class="demo-flat-button" icon="thumb_up"/>
                  <mu-flat-button :label="item.vote_down" class="demo-flat-button" icon="thumb_down"/>
                -->

                  <p style="width: 33%">&nbsp;<b>{{ item.releaseCN }}</b>&nbsp;前发布</p>
                  <p style="width: 33%">浏览&nbsp;<b>{{ item.view_count }}</b>&nbsp;次</p>
                  <p style="width: 33%">将于&nbsp;<b>{{ item.expireCN }}</b>&nbsp;后过期</p>
                </mu-card-actions>
              </a>
            </mu-card>
          </template>
        </mu-list>
      </div>
      <mu-infinite-scroll :scroller="scroller" :loading="loading" @load="loadMore"/>

      <!-- 底部 -->
      <p>总数 {{ total }}</p>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'

export default {
  name: 'app',
  data () {
    return {
      bottomSheet1: false,
      bottomSheet2: false,
      bottomSheet3: false,
      bottomSheet4: false,
      list: [], // 数据
      num: 10, // 每页显示个数
      loading: false, // 加载中图标
      scroller: null, // 页面上可滚动的元素
      total: 0, // 列表数据总数
      openDrawer: false, // 是否打开右侧抽屉
      docked: true, //是否遮罩页面
      // 类目条件
      platformItem: '',
      roleItem: '',
      workItem: '',
      cityItem: '',
      // 类目标题
      platformTitle: '平台',
      roleTitle: '角色',
      workTitle: '工作',
      cityTitle: '城市',
      activeTab: 'release_date',
      sort: '&sb=release_date&sd=desc', // 排序条件
      // 排序按钮样式
      sortActive: '',
      sortDeactive: '',
      sortTab1Style: '',
      sortTab2Style: '',
      sortTab3Style: '',
      keywords: '', // 搜索框内的关键词
      pageNum: 1, // 当前页码
      pageSize: 10, // 每页数据数量
      endPage: false, // 最后一页
      showDetail: false,
      url: '' // 组装搜索的 URL
    }
  },
  beforeMount() {
    Vue.http.get(this.url).then(response => {
      for (let i = 0; i < response.data.data.length; i++) {
        response.data.data[i].releaseCN = this.parseTime(response.data.data[i].release_date)
        response.data.data[i].expireCN = this.parseTime(response.data.data[i].expire_date)
        response.data.data[i].chips = []
        if (typeof(response.data.data[i].categories) != "undefined") { 
          for (let j = 0; j < response.data.data[i].categories.length; j++) {
            response.data.data[i].chips.push(response.data.data[i].categories[j])
          }
        }
        if (typeof(response.data.data[i].roles) != "undefined") { 
          for (let j = 0; j < response.data.data[i].roles.length; j++) {
            response.data.data[i].chips.push(response.data.data[i].roles[j])
          }
        }
        if (typeof(response.data.data[i].skills) != "undefined") { 
          for (let j = 0; j < response.data.data[i].skills.length; j++) {
            response.data.data[i].chips.push(response.data.data[i].skills[j])
          }
        }
        if (typeof(response.data.data[i].city) != "undefined" && response.data.data[i].city != '' && response.data.data[i].city != null) { 
            response.data.data[i].chips.push({name: response.data.data[i].city})
        }
        if (typeof(response.data.data[i].abstract) != "undefined" && response.data.data[i].abstract != '') { 
            response.data.data[i].abstract = response.data.data[i].abstract.substring(0, 50)
        }
        if (typeof(response.data.data[i].price) != "undefined" && response.data.data[i].price != '') { 
            response.data.data[i].price = this.outputdollars(response.data.data[i].price + '')
        } else {
            response.data.data[i].price = '未报价'
        }
      }
      this.list = response.data.data
      console.log(this.list)
      this.total = response.data.total
    }, response => {
      // console.log('error')
    })
  },
  mounted () {
    this.scroller = this.$el
  },
  created () {
    // 处理直接访问详情页的情况
    // console.log(this.$route)
    if (this.$route.name == 'detail') {
      this.$router.push({ name: 'detail', params: { userId: this.$route.params.id }})
      this.showDetail = true
    }

    this.sortActive = 'sort-active'
    this.sortDeactive = 'sort-deactive'
    this.sortTab1Style = this.sortActive
    this.sortTab2Style = this.sortDeactive
    this.sortTab3Style = this.sortDeactive
    this.url = 'https://remotex.ooclab.org/api/jobx/job?sb=release_date&sd=desc&lm=' + this.pageSize
  },
  methods: {
    parseTime(date) {
      if (typeof(date) == "undefined" || date == null) {
        return '180天'
      }
      var now = Date.now()
      var duration = Math.abs(new Date(date) - now)
      var nD = Math.floor(duration/(1000 * 60 * 60 * 24))
      if (nD > 0) {
        return nD + '天'
      } else {
        var nH  = Math.floor(duration/(1000 * 60 * 60))
        if (nH > 0) {
          return nH + '小时'
        } else {
          var nM = Math.floor(duration/(1000 * 60))
          if (nM > 0) {
            return nM + '分钟'
          } else {
            var nS = Math.floor(duration/(1000))
            if (nS > 0) {
              return nS + '秒'
            }
          }
        }

      }
    },
    outputdollars(number) {
      console.log(number)
      if (number == '0' || number == 0) {
        return '无报价'
      }
      if (number.length <= 3)
          return (number == '' ? '0' : number);
      else {
          var mod = number.length % 3;
          var output = (mod == 0 ? '' : (number.substring(0, mod)));
          for (var i = 0; i < Math.floor(number.length / 3); i++) {
              if ((mod == 0) && (i == 0))
                  output += number.substring(mod + 3 * i, mod + 3 * i + 3);
              else
                  output += ',' + number.substring(mod + 3 * i, mod + 3 * i + 3);
          }
          return (output + ' 元');
      }
    },
    closeBottomSheet1 () {
      this.bottomSheet1 = false
    },
    openBottomSheet1 () {
      this.bottomSheet1 = true
    },
    closeBottomSheet2 () {
      this.bottomSheet2 = false
    },
    openBottomSheet2 () {
      this.bottomSheet2 = true
    },
    closeBottomSheet3 () {
      this.bottomSheet3 = false
    },
    openBottomSheet3 () {
      this.bottomSheet3 = true
    },
    closeBottomSheet4 () {
      this.bottomSheet4 = false
    },
    openBottomSheet4 () {
      this.bottomSheet4 = true
    },
    // 加载更多列表数据
    loadMore () {
      if (!this.endPage){
        this.loading = true
        this.pageNum = this.pageNum + 1
        setTimeout(() => {
          Vue.http.get(this.url + '&p=' + this.pageNum).then(response => {
            if (response.data.data.length == 0){
              this.endPage = true
            } else {
              for (let i = 0; i < response.data.data.length; i++) {
                response.data.data[i].releaseCN = this.parseTime(response.data.data[i].release_date)
                response.data.data[i].expireCN = this.parseTime(response.data.data[i].expire_date)
                response.data.data[i].chips = []
                if (typeof(response.data.data[i].categories) != "undefined") { 
                  for (let j = 0; j < response.data.data[i].categories.length; j++) {
                    response.data.data[i].chips.push(response.data.data[i].categories[j])
                  }
                }
                if (typeof(response.data.data[i].roles) != "undefined") { 
                  for (let j = 0; j < response.data.data[i].roles.length; j++) {
                    response.data.data[i].chips.push(response.data.data[i].roles[j])
                  }
                }
                if (typeof(response.data.data[i].skills) != "undefined") { 
                  for (let j = 0; j < response.data.data[i].skills.length; j++) {
                    response.data.data[i].chips.push(response.data.data[i].skills[j])
                  }
                }
                if (typeof(response.data.data[i].city) != "undefined" && response.data.data[i].city != '' && response.data.data[i].city != null) { 
                    response.data.data[i].chips.push({name: response.data.data[i].city})
                }
                if (typeof(response.data.data[i].abstract) != "undefined" && response.data.data[i].abstract != '') { 
                    response.data.data[i].abstract = response.data.data[i].abstract.substring(0, 50)
                }
                if (typeof(response.data.data[i].price) != "undefined" && response.data.data[i].price != '') { 
                    response.data.data[i].price = this.outputdollars(response.data.data[i].price + '')
                } else {
                    response.data.data[i].price = '未报价'
                }
                this.list.push(response.data.data[i])
              }
              this.endPage = false
            }
            this.total = response.data.total
            this.loading = false
          }, response => {
            // console.log('error')
            this.loading = false
            this.endPage = true
          })
        }, 500)
      }
    },
    // 打开、关闭抽屉
    toggleDrawer (flag) {
      this.openDrawer = !this.openDrawer
      this.docked = !flag
      console.log(this.parseTime('2017-04-25T00:00:00.1493049600Z'))
    },
    // 重新加载列表数据
    search () {
      this.list = []
      this.loading = true
      this.pageNum = 1
      this.endPage = false
      this.url = 'https://remotex.ooclab.org/api/jobx/job?' + this.platformItem + this.roleItem + this.workItem + this.cityItem + this.sort + this.keywords + '&lm=' + this.pageSize
      Vue.http.get(this.url).then(response => {
        for (let i = 0; i < response.data.data.length; i++) {
          console.log(response)
          response.data.data[i].releaseCN = this.parseTime(response.data.data[i].release_date)
          response.data.data[i].expireCN = this.parseTime(response.data.data[i].expire_date)
          response.data.data[i].chips = []
          if (typeof(response.data.data[i].categories) != "undefined") { 
            for (let j = 0; j < response.data.data[i].categories.length; j++) {
              response.data.data[i].chips.push(response.data.data[i].categories[j])
            }
          }
          if (typeof(response.data.data[i].roles) != "undefined") { 
            for (let j = 0; j < response.data.data[i].roles.length; j++) {
              response.data.data[i].chips.push(response.data.data[i].roles[j])
            }
          }
          if (typeof(response.data.data[i].skills) != "undefined") { 
            for (let j = 0; j < response.data.data[i].skills.length; j++) {
              response.data.data[i].chips.push(response.data.data[i].skills[j])
            }
          }
          if (typeof(response.data.data[i].city) != "undefined" && response.data.data[i].city != '' && response.data.data[i].city != null) { 
              response.data.data[i].chips.push({name: response.data.data[i].city})
          }
          if (typeof(response.data.data[i].abstract) != "undefined" && response.data.data[i].abstract != '') { 
              response.data.data[i].abstract = response.data.data[i].abstract.substring(0, 50)
          }
          if (typeof(response.data.data[i].price) != "undefined" && response.data.data[i].price != '') { 
              response.data.data[i].price = this.outputdollars(response.data.data[i].price + '')
          } else {
              response.data.data[i].price = '未报价'
          }
        }
        this.list = response.data.data
        this.total = response.data.total
        this.loading = false
      }, response => {
        // console.log('error')
        this.loading = false
      })
    },
    // 点击类目按钮
    categoryItemClick (lk, lv, title) {
      if (lk == 'platform') {
          this.platformItem = ''
          this.platformTitle = title
      } else if (lk == 'role') {
        this.roleItem = ''
        this.roleTitle = title
      } else if (lk == 'work') {
        this.workItem = ''
        this.workTitle = title
      } else if (lk == 'city') {
        this.cityItem = ''
        this.cityTitle = title
      }
      if (lv != '0') {
        if (lk == 'platform') {
          this.platformItem = '&' + lk + '=' + lv
        } else if (lk == 'role') {
          this.roleItem = '&' + lk + '=' + lv
        } else if (lk == 'work') {
          this.workItem = '&' + lk + '=' + lv
        } else if (lk == 'city') {
          this.cityItem = '&' + lk + '=' + lv
        }
      }
      this.search()
    },
    // 点击排序按钮
    sortItemClick (sb) {
      this.activeTab = sb
      this.sort = '&sb=' + sb + '&sd=desc'
      this.sortTab1Style = this.sortDeactive
      this.sortTab2Style = this.sortDeactive
      this.sortTab3Style = this.sortDeactive
      if (sb == 'release_date'){
        this.sortTab1Style = this.sortActive
      } else if (sb == 'view_count'){
        this.sortTab2Style = this.sortActive
      } else if (sb == 'price'){
        this.sortTab3Style = this.sortActive
      } 
      this.search()
    },
    // 搜索框事件
    textChanged (e) {
      var textValue = e.target.value
      if (textValue == '') {
        this.keywords = ''
      } else {
        this.keywords = '&lk=title&lv=' + e.target.value
      }
    },
    // 打开详情页
    openDetailPopup (id) {
      // this.$router.push({ path: '/detail/' + id })
      // this.showDetail = true
      Vue.http.get('https://remotex.ooclab.org/api/jobx/job/' + id).then(response => {
      }, response => {
      })
    },
    // 关闭详情页
    closeDetailPopup(){
      this.$router.back()
      this.showDetail = false
    }
  }
}
</script>

<style>
html, body {
  height: 100%;
  width: 100%;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  overflow: auto;
  text-align:center;
  -webkit-overflow-scrolling: touch;
}

#home {
  max-width: 736px;
  margin:0 auto;
}

#tabs {
  background: #ededed;
  margin-top: 10px;
}

#sort-deactive {
  color: #616161;
}

#sort-active {
  color: #F5193E;
}

.page-infinite-listitem {
  /*height: 130px;*/
  line-height: 16px;
  text-align: left;
  display: block;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}


</style>
