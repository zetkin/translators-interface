const fetchWrapper = async (params) => {
  const requestOptions = {
    // Defaults
    method: params.method || 'GET',
    // Custom options
    body: params.body,
    // Request headers
    headers: {
      'Content-Type': 'application/json',
      // Unpack other headers
      ...(params.headers && params.headers),
      ...(params.token && { Authorization: params.token }),
    },
  }

  // Make request
  const resp = await fetch(params.url, requestOptions)

  // If not a success code
  if (!resp.ok) throw new Error('Error making request')

  // If a successful response code
  try {
    // Parse json
    const body = await resp.json()
    return body
  } catch (err) {
    console.error(err)
    // If no body content
    return undefined
  }
}

export default fetchWrapper
