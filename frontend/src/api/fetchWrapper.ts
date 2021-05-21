class APIError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'APIError'
  }
}

interface AuthFetchParams {
  url: string
  method?: 'GET' | 'POST' | 'DELETE' | 'PUT' | 'PATCH'
  body?: any
  token?: string
  headers?: { [key: string]: string }
}

const fetchWrapper = async <G>(
  params: AuthFetchParams
): Promise<G | undefined> => {
  const requestOptions: RequestInit = {
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
  if (!resp.ok) {
    // Check if there's response data
    try {
      const body = await resp.json()
      // If response data, throw error with error string from backend
      throw new APIError(body)
    } catch (err) {
      // If the error is an APIError, throw it
      if (err instanceof APIError) throw err
      // If no response data, throw default response error
      throw new Error('Error making request')
    }
  }

  // If a successful response code
  try {
    // Parse json
    const body = (await resp.json()) as G
    return body
  } catch (err) {
    // If no body content
    return undefined
  }
}

export default fetchWrapper
