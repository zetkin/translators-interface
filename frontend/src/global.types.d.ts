// Backend Models

export interface Project {
  id: number
  name: string
  repository_name: string
  locale_files_path: string
  languages: Language[]
}

export interface Language {
  id: number
  name: string
  language_code: string
}

export interface Translation {
  id: string
  text: string
  author: string
  from_repository: boolean
  created_at: Date
  file_path: string
  object_path: string
  dotpath: string
  project: number // Foreign key to the project id
  language: Language
}
