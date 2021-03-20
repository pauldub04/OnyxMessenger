import createPersistedState from 'vuex-persistedstate'

export default ({ store }) => {
  createPersistedState({
    key: 'vuex-persistedstate',
    // paths: ['user', 'token'],
    storage: window.sessionStorage,
  })(store)
}
