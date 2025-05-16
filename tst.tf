provider "aws" {
  region     = "us-east-1"
  access_key = "AKIA47CRWATFXDOP2TWP"
  secret_key = "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"
}

resource "aws_s3_bucket" "website_bucket" {
  bucket         = "leader-chemico"
  force_destroy  = true
}

resource "aws_s3_bucket_website_configuration" "website_config" {
  bucket = aws_s3_bucket.website_bucket.id

  index_document {
    suffix = "index.html"
  }

  error_document {
    key = "index.html"
  }
}

resource "aws_s3_bucket_policy" "allow_public_read" {
  bucket = aws_s3_bucket.website_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "PublicReadGetObject"
        Effect    = "Allow"
        Principal = "*"
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.website_bucket.arn}/*"
      }
    ]
  })
}

locals {
  files = fileset("${path.module}/site", "**/*.*")

  mime_types = {
    html = "text/html"
    css  = "text/css"
    js   = "application/javascript"
    png  = "image/png"
    jpg  = "image/jpeg"
    jpeg = "image/jpeg"
    svg  = "image/svg+xml"
  }
}

resource "aws_s3_object" "website_files" {
  for_each = { for file in local.files : file => file }

  bucket       = aws_s3_bucket.website_bucket.id
  key          = each.key
  source       = "${path.module}/site/${each.key}"
  content_type = lookup(local.mime_types, lower(split(".", each.key)[length(split(".", each.key)) - 1]), "application/octet-stream")
}

output "website_url" {
  value = aws_s3_bucket_website_configuration.website_config.website_endpoint
}
