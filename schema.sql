CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR NOT NULL,
    email VARCHAR NOT NULL UNIQUE,
    aadhaar_application_id VARCHAR NOT NULL UNIQUE,
    phone_number BIGINT NOT NULL,
    address TEXT,
    dob DATE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX ix_users_email ON users (email);
CREATE INDEX ix_users_aadhaar_application_id ON users (aadhaar_application_id);
