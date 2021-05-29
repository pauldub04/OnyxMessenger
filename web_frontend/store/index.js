import colors from 'vuetify/es5/util/colors'

/* eslint-disable */
export const state = () => ({
  user: {
    username: '',
    email: '',
    id: '',
  },
  token: null,
  status: '',

  chat: {
    selected_chat: -1,
  }
})

export const mutations = {
  setUser(state, user) {
    state.user = user
  },
  setToken(state, token) {
    state.token = token;
  }

}

export const actions = {
  async signUp(ctx, credentials) {
    return this.$axios
      .post('http://localhost:8000/auth/users/', credentials)
      .then((response) => {
        console.log('signed up')
        console.log(response.data)
        alert('Your account has been created. You will be signed in automatically')
        ctx.dispatch('signIn', credentials)
      })
      .catch((error) => {
        console.log(error.response)
        alert(error.response.request.response)
      })
  },

  async signIn(ctx, credentials) {
    return this.$axios
        .post('http://localhost:8000/auth/token/login/', credentials)
        .then(async (response) => {
          console.log('signed in')
          console.log(response.data)

          ctx.dispatch('setAuthHeader', response.data.auth_token);
          ctx.commit('setToken', response.data.auth_token);
          await ctx.dispatch('fetchUser')
          
          console.log('fetched, pushing')
          this.$router.push(this.localePath('/main'))
        })
        .catch((error) => {
          console.log(error.response)
          alert(error.response.request.response)
        })
  },
  async fetchUser(ctx) {
    return this.$axios
      .get('http://localhost:8000/auth/users/me/')
      .then((response) => {
        console.log('fetch user start')
        console.log(response.data)

        let user = {
          username: response.data.username,
          id: response.data.id,
          email: response.data.email,
        }
        ctx.commit('setUser', user)

        console.log('fetch user stop')
      })
      .catch((error) => {
        console.log(error.response)
        alert(error.response.request.response)
      })
  },
  logOut(ctx) {
    this.$axios
      .post('http://localhost:8000/auth/token/logout/')
      .then((response) => {
        console.log('logout')
        console.log(response.data)

        ctx.commit('setUser', {})
        ctx.commit('setToken', null)
        this.$router.push('/')
      })
      .catch((error) => {
        console.log(error)
        ctx.commit('setUser', {})
        ctx.commit('setToken', null)
        this.$router.push('/')
      })

  },

  setAuthHeader(ctx, token) {
    this.$axios.setToken(token, 'Token ');
  },

  middlewareAuthMain(ctx) {
    if (ctx.state.token === null || ctx.state.token === '') {
      this.$router.push('/')
    }
  },
  middlewareAuthSign(ctx) {
    if (ctx.state.token !== null && ctx.state.token !== '') {
      this.$router.push('/main')
    }
  },
  setTheme(ctx, i18n) {
    window.$nuxt.$root.$vuetify.theme.dark = JSON.parse(localStorage.getItem('dark_theme')) || 0;

    const default_theme = {
      name: 'Base Theme',
      dark: {
        primary: colors.blue.darken2,
        accent: colors.grey.darken3,
        secondary: colors.amber.darken3,
        info: colors.teal.lighten1,
        warning: colors.amber.base,
        error: colors.deepOrange.accent4,
        success: colors.green.accent3,
      },
      light: {
        primary: colors.blue.darken2,
        accent: colors.grey.darken3,
        secondary: colors.amber.darken3,
        info: colors.teal.lighten1,
        warning: colors.amber.base,
        error: colors.deepOrange.accent4,
        success: colors.green.accent3,
      },
    }
    const theme = JSON.parse(localStorage.getItem('theme')) || default_theme;
    const name = theme.name
    const dark = theme.dark
    const light = theme.light
    // set themes
    Object.keys(dark).forEach((i) => {
      window.$nuxt.$root.$vuetify.theme.themes.dark[i] = dark[i]
    })
    Object.keys(light).forEach((i) => {
      window.$nuxt.$root.$vuetify.theme.themes.light[i] = light[i]
    })
    // also save theme name to disable selection
    window.$nuxt.$root.$vuetify.theme.themes.name = name

    const locale = JSON.parse(localStorage.getItem('locale'))
    i18n.setLocale(locale)
  }
}

export const getters = {
  getUser(state) {
    return state.user;
  },
  getToken(state) {
    return state.token;
  }
}