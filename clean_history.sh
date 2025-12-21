#!/bin/bash
if [ -f LibraryManagementSystem/LibraryManagementSystem/settings.py ]; then
    sed -i 's/EMAIL_HOST_USER = '\''mithunkumarrajak01012005@gmail.com'\''/EMAIL_HOST_USER = os.getenv('\''EMAIL_HOST_USER'\'')/g' LibraryManagementSystem/LibraryManagementSystem/settings.py
    sed -i 's/EMAIL_HOST_PASSWORD = '\''wpqu syjc etub fknb'\''/EMAIL_HOST_PASSWORD = os.getenv('\''EMAIL_HOST_PASSWORD'\'')/g' LibraryManagementSystem/LibraryManagementSystem/settings.py
fi
if [ -f LibraryManagementSystem/LibraryManagementSystem/views.py ]; then
    sed -i 's/'\''mithunkumarrajak18plus@gmail.com'\''/'\''test@example.com'\''/g' LibraryManagementSystem/LibraryManagementSystem/views.py
fi