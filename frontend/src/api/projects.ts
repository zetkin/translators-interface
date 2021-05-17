import { Project } from '../global.types'
import fetchWrapper from './fetchWrapper'

export const getProjects = async (): Promise<Project[]> => {
  return fetchWrapper({ url: `http://${process.env.NEXT_PUBLIC_API_HOST}/projects/` })
}

export const getProject = async (projectId): Promise<Project> => {
  return fetchWrapper({ url: `http://${process.env.NEXT_PUBLIC_API_HOST}/projects/${projectId}/` })
}
