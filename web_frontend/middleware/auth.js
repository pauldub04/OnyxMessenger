export default function ({ store, redirect }) {
  // eslint-disable-next-line no-console
  console.log('middleware, token = ')
  // eslint-disable-next-line no-console
  console.log(store.state.token)
  if (store.state.token === null || store.state.token === '') {
    return redirect('/')
  }
}
