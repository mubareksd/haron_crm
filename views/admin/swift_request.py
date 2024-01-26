from flask import render_template, redirect, request

from models import CNC, storage
from views.admin import admin_view


@admin_view.route('/swift_request/<swift_request_id>', methods=['GET', 'POST'], strict_slashes=False)
def swift_request(swift_request_id):
    if request.method == 'POST':
        swift_request_obj = storage.get('SwiftRequest', swift_request_id)
        swift_request_obj.bm_update(
            business_name=request.form.get('business_name'),
            contact_name=request.form.get('contact_name'),
            contact_email=request.form.get('contact_email'),
            contact_phone=request.form.get('contact_phone'),
            contact_address=request.form.get('contact_address'),
            contact_city=request.form.get('contact_city'),
            contact_state=request.form.get('contact_state'),
            contact_zip=request.form.get('contact_zip'),
            contact_country=request.form.get('contact_country'),
            status=request.form.get('status'),
        )
        return redirect('/admin')
    form_fields = [
        {
            'label': 'Business Name',
            'id': 'business_name',
            'name': 'business_name',
            'type': 'text',
            'help_text': 'Enter the name of the business you are requesting a Swift account for.'
        },
        {
            'label': 'Contact Name',
            'id': 'contact_name',
            'name': 'contact_name',
            'type': 'text',
            'help_text': 'Enter the name of the person who will be the primary contact for this account.'
        },
        {
            'label': 'Contact Email',
            'id': 'contact_email',
            'name': 'contact_email',
            'type': 'email',
            'help_text': 'Enter the email address of the primary contact for this account.'
        },
        {
            'label': 'Contact Phone',
            'id': 'contact_phone',
            'name': 'contact_phone',
            'type': 'tel',
            'help_text': 'Enter the phone number of the primary contact for this account.'
        },
        {
            'label': 'Contact Address',
            'id': 'contact_address',
            'name': 'contact_address',
            'type': 'text',
            'help_text': 'Enter the street address of the primary contact for this account.'
        },
        {
            'label': 'Contact City',
            'id': 'contact_city',
            'name': 'contact_city',
            'type': 'text',
            'help_text': 'Enter the city of the primary contact for this account.'
        },
        {
            'label': 'Contact State',
            'id': 'contact_state',
            'name': 'contact_state',
            'type': 'text',
            'help_text': 'Enter the state / province of the primary contact for this account.'
        },
        {
            'label': 'Contact Zip',
            'id': 'contact_zip',
            'name': 'contact_zip',
            'type': 'text',
            'help_text': 'Enter the zip code / Postal Code of the primary contact for this account.'
        },
        {
            'label': 'Contact Country',
            'id': 'contact_country',
            'name': 'contact_country',
            'type': 'text',
            'help_text': 'Enter the country of the primary contact for this account.'
        },
        {
            'label': 'Status',
            'id': 'status',
            'name': 'status',
            'type': 'selector',
            'options': [
                {
                    'value': 'Pending',
                },
                {
                    'value': 'Denied',
                },
                {
                    'value': 'Approved',
                },
            ],
            'help_text': 'Select the status of this request.',
        },
    ]
    swift_request = storage.get('SwiftRequest', swift_request_id)

    for field in form_fields:
        field['value'] = getattr(swift_request, field['name'])


    return render_template(
        'swift_request.html', form_fields=form_fields,
        page={
            'title': 'Swift Request',
        },
        form={
            'action': '/admin/swift_request/' + swift_request_id,
            'method': 'POST'
        },
    )
